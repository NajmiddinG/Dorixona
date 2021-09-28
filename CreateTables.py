import sqlite3

conn = sqlite3.connect('dorixona.db')
cur = conn.cursor()

# xodimlar
cur.execute(""" create table if not exists xodim(
        id integer primary key autoincrement,
        ism varchar(100) not null,
        familiya varchar(100),
        rasm varchar(200),
        oylig integer not null,
        balans integer not null,
        kasbi varchar(100),
        tell integer (100),
        manzil varchar(255) not null,
        qoshimcha varchar(255)
    );""")

# kashalog
cur.execute(""" create table if not exists kashalog(
        id integer primary key autoincrement,
        dori_nomi varchar(100) not null,
        pachka_soni integer(3) not null,
        narx integer not null,
        barcode integer not null unique,
        qoshimcha varchar(200)
    )""")

# dori olish
cur.execute(""" create table if not exists mahsulot_olish(
        id integer primary key autoincrement,
        xodim integer not null,
        firma varchar(100),
        sana text not null,
        balans integer not null,
        tel integer,
        qoshimcha varchar(200),
        foreign key (xodim) references xodim(id) on delete set null
    );""")

cur.execute(""" create table if not exists olingan_dori(
        id integer primary key autoincrement,
        dori_id integer not null,
        missiya_id integer not null,
        tannarx integer,
        barcode integer not null,
        pachka_soni integer not null,
        qoshimcha varchar(200),
        foreign key (missiya_id) references mahsulot_olish(id) on delete set null,
        foreign key (dori_id) references kashalog(id) on delete set null,
        foreign key (tannarx) references kashalog(narx) on delete set null,
        foreign key (barcode) references kashalog(barcode) on delete set null,
        foreign key (pachka_soni) references kashalog(pachka_soni) on delete set null
    );""")

# ombor
cur.execute(""" create table if not exists ombor(
        id integer primary key autoincrement,
        dori_id integer not null,
        narx integer,
        tannarx integer,
        qolgani integer,
        kelgan_sana text,
        foreign key (dori_id) references kashalog(id) on delete set null,
        foreign key (tannarx) references olingan_dori(tannarx) on delete set null,
        foreign key (dori_id) references kashalog(id) on delete set null,
        foreign key (narx) references kashalog(narx) on delete set null
    );""")

# qaytarib_olish
cur.execute("""create table if not exists qaytarib_berish(
        id integer primary key autoincrement,
        mahsulot_id integer,
        sana text not null,
        sabab varchar(200),
        foreign key (mahsulot_id) references mahsulot_olish(id) on delete set null 
);""")

# sotuv
cur.execute(""" create table if not exists sotuv(
        id integer primary key autoincrement,
        summa integer,
        sana text not null,
        xodim integer not null,
        foreign key (xodim) references xodim(id) on delete set null
);""")

cur.execute(""" create table if not exists sotilgan_dori(
        id integer primary key autoincrement,
        dori_id integer not null,
        tannarx integer,
        sotish_narx integer,
        foreign key (dori_id) references kashalog(dori_id) on delete set null,
        foreign key (tannarx) references kashaloq(narx) on delete set null
);""")

# Statistika
cur.execute(""" create table if not exists statistika(
        id integer primary key autoincrement,
        kirim integer,
        chiqim integer
);""")
conn.commit()
