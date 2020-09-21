#!/usr/bin/python3

#from flare_lakeformation.permissions import Permissions
from flare_s3replication.replication import Replication 

def main():
    mystatus = Replication("BUCKETNAME", "ACCOUNT ID")
    print(mystatus.status())

if __name__ == "__main__":
    main()
