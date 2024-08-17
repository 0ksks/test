Hostname = "127.0.0.1"
Port = 3306
Username = "username"
Password = "password"
Database = "database"
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{Username}:{Password}@{Hostname}:{Port}/{Database}"  # 最后是数据库名
SQLALCHEMY_TRACK_MODIFICATIONS = False
