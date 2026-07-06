# simple-url-shortener
This is a simple containerized URL shortener application based on production grade URL shortening applications like bitly<br>
Not deployed yet WIP <br>
## Architecture
API server : FastAPI <br>
Database + Read Replica : PostgreSQL <br> Current schema -
![database-diag](./db_diagram.png)<br>
Cache : Redis <br>

## Work plan
<ul>
<li>Add proper APIs + logic</li>
<li>Add NGINX reverse proxy</li>
<li>Grafana for monitnoring</li>
</ul>