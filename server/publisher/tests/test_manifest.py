import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import manifest as mf  # noqa: E402

SP = timezone(timedelta(hours=-3))


def write(tmp: Path, folder: str, data: dict, files=("video.mp4", "thumbnail.png", "legendas.srt")):
    d = tmp / folder
    d.mkdir(parents=True, exist_ok=True)
    for f in files:
        (d / f).write_bytes(b"x")
    (d / "publish.json").write_text(json.dumps(data))
    return d


def base(key="ptd-ep07-long", **kw):
    item = {"key": key, "kind": "long", "video": ["video.mp4"], "title": "Título <teste> -> ok",
            "description": "desc", "tags": ["a", "b, c"], "thumbnail": "thumbnail.png", "captions": "legendas.srt",
            "publish_at": "2026-11-08T18:00:00-03:00"}
    item.update(kw)
    return {"version": 1, "channel_id": "UCd_BGmJ5gbQ0kECAxmbvQHA", "created_at": "2026-11-07T15:00:00-03:00",
            "items": [item]}


def test_discover_and_clean(tmp_path):
    write(tmp_path, "ep07", base())
    write(tmp_path, "server/x", base("ignored"))  # server/ é ignorado
    items, errors = mf.discover(tmp_path)
    assert errors == []
    assert [i.key for i in items] == ["ptd-ep07-long"]
    it = items[0]
    assert it.clean_title() == "Título ‹teste› → ok"
    assert it.clean_tags() == ["a", "b  c"]
    assert it.missing_files() == []
    assert it.publish_at == datetime(2026, 11, 8, 18, 0, tzinfo=SP)


def test_duplicate_keys_and_bad_json(tmp_path):
    write(tmp_path, "a", base("dup"))
    write(tmp_path, "b", base("dup"))
    (tmp_path / "c").mkdir()
    (tmp_path / "c" / "publish.json").write_text("{nope")
    items, errors = mf.discover(tmp_path)
    assert len(items) == 1
    assert any("repetida" in e for e in errors)
    assert any("JSON inválido" in e for e in errors)


def test_naive_date_rejected(tmp_path):
    write(tmp_path, "a", base(publish_at="2026-11-08T18:00:00"))
    items, errors = mf.discover(tmp_path)
    assert items == [] and "fuso" in errors[0]


def test_decide_rules(tmp_path):
    write(tmp_path, "a", base())
    it = mf.discover(tmp_path)[0][0]
    grace = timedelta(minutes=90)
    # dentro da carência
    assert mf.decide(it, {}, datetime(2026, 11, 7, 15, 30, tzinfo=SP), grace).action == "wait"
    # agenda no futuro
    d = mf.decide(it, {}, datetime(2026, 11, 7, 20, 0, tzinfo=SP), grace)
    assert (d.action, d.visibility) == ("upload", "schedule")
    # horário passou → público agora
    d = mf.decide(it, {}, datetime(2026, 11, 8, 17, 50, tzinfo=SP), grace)
    assert (d.action, d.visibility) == ("upload", "public")
    # já publicado / done_url / 3 erros
    assert mf.decide(it, {it.key: {"status": "published"}}, datetime(2026, 11, 8, tzinfo=SP), grace).action == "done"
    assert mf.decide(it, {it.key: {"status": "error", "attempts": 3}}, datetime(2026, 11, 8, tzinfo=SP), grace).action == "skip"
    it.done_url = "https://youtu.be/x"
    assert mf.decide(it, {}, datetime(2026, 11, 8, tzinfo=SP), grace).action == "done"


def test_if_late_skip_and_parts(tmp_path):
    write(tmp_path, "q", base("quiet-ep02-long", video=["video.part00", "video.part01"], if_late="skip"),
          files=("video.part00", "video.part01", "thumbnail.png", "legendas.srt"))
    it = mf.discover(tmp_path)[0][0]
    assert len(it.video_paths()) == 2
    d = mf.decide(it, {}, datetime(2026, 11, 9, tzinfo=SP), timedelta(0))
    assert d.action == "skip"


def test_missing_file_reported(tmp_path):
    write(tmp_path, "a", base(), files=("video.mp4",))
    it = mf.discover(tmp_path)[0][0]
    assert len(it.missing_files()) == 2
