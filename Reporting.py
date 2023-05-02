import sqlite3

con = sqlite3.connect("tutorial.db")

con = sqlite3.connect(":memory:")

cur = con.cursor()

cur.execute("create table WARM_BOOT(ATTEMPTS, XTREAM_PAGE, ANDROID_PAGE, ONBOARDING_PAGE, HOME_PAGE)")


cur.execute("insert into WARM_BOOT values (?, ?, ?, ?, ?)", (1, 'NA','NA','45.94','68' ))

for row in cur.execute("select * from WARM_BOOT"):
        print(row)

con.commit()

# cur.execute('DROP TABLE WARM_BOOT')

con.close()