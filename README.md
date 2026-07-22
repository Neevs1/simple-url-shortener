# simple-url-shortener
This is a simple containerized URL shortener application based on production grade URL shortening applications like bitly<br>
Not deployed yet WIP <br>
## Architecture
API server : FastAPI <br>
Database + Read Replica : PostgreSQL <br> Current schema -
![database-diag](./db_diagram.png)<br>
Cache : Redis <br>

## Url generation logic
URL generation is based on Base62 + counter. By using the unique id of each original url, a short url is created.

## Cache Population
Cache will be populated using eager population. The understanding behind this is that urls will be used more after creation.<br>
For expired URLs lazy population will be used.

## Cache invalidation strategy
Each URL will have TTL = 7 days.

## Work plan
<ul>
<li>Add final APIs</li>
<li>Add NGINX reverse proxy</li>
<li>Grafana for monitnoring</li>
</ul>