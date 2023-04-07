import sqlite3, pytz, os, subprocess
from datetime import datetime

# This is my first attempt to create a python class this might not work as expected
class GravityDatabase:
    def __init__(self, database="/etc/pihole/gravity.db", comment="pam-enabled"):
        if os.path.isfile(database):
            self.comment = comment
            self.database = database
            self.con = sqlite3.connect(database)
            self.cur = self.con.cursor()
            self.res = self.cur.execute(f"SELECT address, enabled, date_modified FROM adlist WHERE comment='{self.comment}'")
            # fetchall() will return a list of tuple which we will need to merge into a list
            fetch_tuple = self.res.fetchall()
            self.results = list(map(list,fetch_tuple))
            # Add a section to detect the sqlite3 timezone
            for item in self.results:
                date_modified_epoch = item[2]
                datetime_obj = datetime.fromtimestamp(date_modified_epoch)
                item[2] = f"{datetime_obj:%Y/%m/%d %H:%M:%S}"
        else:
            print({"Error": "Database not found"})
            exit()
    def update(self):
        process = subprocess.run(['/etc/.pihole/gravity.sh'], check=True, stdout=subprocess.PIPE, universal_newlines=True)
        output = process.stdout
        return output

    def status(self):
        return self.results

    def toggle(self, is_enabled=True):
        try:
            self.res = self.cur.execute(f"UPDATE adlist SET enabled={int(is_enabled)} where comment='{self.comment}'")
            self.con.commit()
            return {"message": f"Set {len(self.results)} adlist(s) with comment '{self.comment}' to {is_enabled} ({int(is_enabled)})"}
        except sqlite3.Error as err:
            print({"Error": err})


# test = GravityDatabase(database="../gravity.db", comment="Firebog")
# print(test.get_status())
# print(test.toggle(False))
# print(test.get_status())
# print(test.toggle(True))
# print(test.get_status())
