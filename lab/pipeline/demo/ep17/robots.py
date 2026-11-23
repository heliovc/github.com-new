from urllib.robotparser import RobotFileParser

robots = RobotFileParser("http://localhost:8000/robots.txt")
robots.read()

print(robots.can_fetch("*", "http://localhost:8000/catalog/page-1.html"))
print(robots.can_fetch("*", "http://localhost:8000/admin/"))
print(robots.crawl_delay("*"))
