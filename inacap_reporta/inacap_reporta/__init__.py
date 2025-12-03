# PyMySQL must be loaded BEFORE Django tries to connect to MySQL
# This allows Django to use PyMySQL as a drop-in replacement for MySQLdb
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    # PyMySQL not installed, will use mysqlclient if available
    pass

