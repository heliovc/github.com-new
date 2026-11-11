"""EP07 demo: a REAL interactive bash session (pty, 80 columns) run as user alex. Every command in the video is typed here;
output is captured verbatim -> ep07_transcript.txt (sections ### NAME)."""
import os, pty, pwd, shutil, time, select, sys, fcntl, termios, struct, subprocess
U = pwd.getpwnam("alex"); HOME = U.pw_dir
# fresh practice home
for n in os.listdir(HOME):
    p = os.path.join(HOME, n); shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
for f in (".bashrc", ".profile", ".bash_logout"): shutil.copy("/etc/skel/" + f, HOME)
for d in ("Desktop", "Documents", "Downloads", "Documents/school"): os.makedirs(os.path.join(HOME, d))
files = {"notes.txt": "buy milk\ncall mom\n", "Documents/resume.txt": "Alex Doe - resume\n", "Documents/school/essay.txt": "My essay\n",
         "Downloads/beach1.jpg": "jpg", "Downloads/beach2.jpg": "jpg", "Downloads/beach3.jpg": "jpg", "Downloads/ticket.pdf": "pdf"}
for f, c in files.items(): open(os.path.join(HOME, f), "w").write(c)
subprocess.run(["chown", "-R", "alex:alex", HOME], check=True)
os.environ.clear(); os.environ.update(HOME=HOME, USER="alex", TERM="dumb", PATH="/usr/local/bin:/usr/bin:/bin", LANG="C.UTF-8", PS1="__P__", HISTFILE="/dev/null")
os.chdir(HOME)
pid, fd = pty.fork()
if pid == 0:
    os.setgid(U.pw_gid); os.setuid(U.pw_uid)
    os.execvp("bash", ["bash", "--norc", "--noprofile", "-i"])
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 24, 80, 0, 0))
buf = b""
def until_prompt(t=10):
    global buf
    end = time.time() + t
    while b"__P__" not in buf and time.time() < end:
        r, _, _ = select.select([fd], [], [], 0.2)
        if r: buf += os.read(fd, 65536)
    out, _, buf = buf.partition(b"__P__"); return out.decode().replace("\r\n", "\n").replace("\r", "")
until_prompt()
def raw(s): os.write(fd, s.encode()); return until_prompt()
raw("stty -echo cols 80\n")
OUT = []
def run(cmd):
    o = raw(cmd + "\n"); OUT.append("$ " + cmd); OUT.extend(l for l in o.rstrip("\n").split("\n") if o.strip())
def sec(n): OUT.append("### " + n)
sec("pwd"); run("pwd")
sec("ls"); run("ls")
sec("lsl"); run("ls -l")
sec("lsa"); run("ls -a")
sec("cd"); run("cd Documents"); run("pwd"); run("ls")
sec("cdup"); run("cd school"); run("pwd"); run("cd .."); run("pwd"); run("cd ~"); run("pwd")
sec("cdpath"); run("cd Documents/school"); run("pwd"); run("cd ../.."); run("pwd")
sec("mkdir"); run("mkdir trip"); run("cd trip"); run("touch packing.txt budget.txt"); run("ls")
sec("echo"); run("echo \"passport\" > packing.txt"); run("echo \"phone charger\" >> packing.txt"); run("echo \"sunscreen\" >> packing.txt"); run("cat packing.txt")
sec("cp"); run("cp packing.txt packing-backup.txt"); run("ls")
sec("mv"); run("mv budget.txt costs.txt"); run("ls")
sec("mvphotos"); run("mkdir photos"); run("ls ~/Downloads"); run("mv ~/Downloads/*.jpg photos/"); run("ls photos"); run("ls ~/Downloads")
sec("glob"); run("ls *.txt")
sec("rm"); run("rm packing-backup.txt"); run("ls")
sec("rmdir"); run("rm photos"); run("rmdir photos"); run("mkdir old"); run("rmdir old"); run("ls")
sec("err"); run("cd ~"); run("cd Documnets"); run("sl"); run("mkdir trip"); run("cd trip"); run("cat packing")
sec("space"); run("mkdir \"summer plans\""); run("cd summer plans"); run("cd \"summer plans\""); run("pwd"); run("cd .."); run("rmdir \"summer plans\"")
sec("history"); run("history | tail -5")
sec("help"); run("ls --help | head -4")
sec("final"); run("cd ~"); run("ls"); run("ls trip"); run("cat trip/packing.txt")
os.write(fd, b"exit\n"); time.sleep(0.3)
open(sys.argv[1], "w").write("\n".join(OUT) + "\n"); print("ok", len(OUT))
