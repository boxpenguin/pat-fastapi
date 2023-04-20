import sqlite3, pytz, os, subprocess
from datetime import datetime


class GravityDatabase:
    def __init__(self, db_path: str ="/etc/pihole/gravity.db", comment="pat-enabled"):
        # if os.path.isfile(db_path):
        self.db_path = db_path
        try:
            self.comment = comment
            self.con = sqlite3.connect(db_path)
            self.cur = self.con.cursor()
            self.res = self.cur.execute("SELECT address, enabled, date_modified FROM adlist WHERE comment=?", (self.comment,))
            # self.res = self.cur.execute(f"SELECT address, enabled, date_modified FROM adlist WHERE comment='{self.comment}'")
            fetch_tuple = self.res.fetchall()
            self.raw_list = list(map(list,fetch_tuple))
            for item in self.raw_list:
                date_modified_epoch = item[2]
                datetime_obj = datetime.fromtimestamp(date_modified_epoch)
                item[2] = f"{datetime_obj:%Y/%m/%d %H:%M:%S}"
            my_counter = 0
            adlist = {"adlist0": {"address": "", "enabled": "", "date_modified": ""}}
            for each in self.raw_list:
                adlist[f"adlist{my_counter}"] = {"address": each[0], "enabled": each[1], "date_modified": each[2]}
                my_counter += 1
            self.results = adlist 
        except sqlite3.Error as e:
            raise ValueError(f"Error connecting to database: {e}")
        # else:
        #     print({"Error": "Database not found"})
        #     exit()

    def update(self):
        process = subprocess.run(['/etc/.pihole/gravity.sh'], check=True, stdout=subprocess.PIPE, universal_newlines=True)
        output = process.stdout
        return output

    def status(self):
        return self.results

    # TODO: rewrite as two functions
    def toggle(self, is_enabled=True):
        try:
            self.res = self.cur.execute(f"UPDATE adlist SET enabled={int(is_enabled)} where comment='{self.comment}'")
            self.con.commit()
            return {"message": f"Set {len(self.results)} adlist(s) with comment '{self.comment}' to {is_enabled} ({int(is_enabled)})"}
        except sqlite3.Error as err:
            print({"Error": err})

    def enable_adlist(self):
        try:
            self.res = self.cur.execute("UPDATE adlist SET enabled=1 where comment=?", (self.comment,))
            self.con.commit()
            return {"message": f"Set {len(self.results)} adlist(s) with comment '{self.comment}' to ENABLE"}
        except sqlite3.Error as e:
            raise ValueError(f"Unable to Enable {self.comment} due to {e}")
            
    def disable_adlist(self):
        try:
            self.res = self.cur.execute("UPDATE adlist SET enabled=0 where comment=?", (self.comment,))
            self.con.commit()
            return {"message": f"Set {len(self.results)} adlist(s) with comment '{self.comment}' to DISABLE"}
        except sqlite3.Error as e:
            raise ValueError(f"Unable to Enable {self.comment} due to {e}")
