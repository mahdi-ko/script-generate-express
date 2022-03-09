import os
import database
root = "Server"
os.makedirs(root, exist_ok=True)
os.makedirs("%s/Controller" % root, exist_ok=True)
os.makedirs('%s/Routes' % root, exist_ok=True)
os.makedirs('%s/Database' % root, exist_ok=True)

with open('%s/Database/database.js' % root, "a+") as f:
    f.write(database.database_connect())

with open('%s/server.js' % root, "a+") as f:
    f.write("dummy")
