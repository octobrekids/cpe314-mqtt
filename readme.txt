MacOS
    รันผ่าน Terminal โดยใช้ Python3
    1. Broker Program
        1.1 เปิดหน้าต่าง Terminal ใหม่ เข้าไปยังโฟลเดอร์ที่เก็บไฟล์ไว้ 
        1.2 Run Broker Program ผ่านคำสั่ง 'Python3 broker.py'
        1.3 เมื่อโปรแกรม Run จะมีการแสดงผลของ Broker IP นั้น ๆ (สำหรับใช้ในการ Connect จาก subscribe หรือ Publisher)
        1.4 หากผู้ใช้ต้องการจบโปรแกรม ให้ทำการ Ctrl+C หรือทำการปิดหน้าต่าง Terminal
    2. Subscriber Program
        2.1 เปิดหน้าต่าง Terminal ใหม่ เข้าไปยังโฟลเดอร์ที่เก็บไฟล์ไว้ 
        2.2 Run Subscribe Program ผ่านคำสั่ง 'Python3 Subscribe.py'
        2.3 พิมพ์คำสั่งตาม Format ทืี่กำหนดในโปรแกรม 'Subscribe <broker_ip_address> <topic_name>'
        2.4 เปิดหน้าต่าง ​Terminal ค้างไว้ เพื่อรอรับข้อมูลที่ได้ทำการ Subscribe ไว้
        2.5 หากผู้ใช้ต้องการจบโปรแกรม ให้ทำการ Ctrl+C หรือทำการปิดหน้าต่าง Terminal
    3. Publisher Program
        3.1 เปิดหน้าต่าง Terminal ใหม่ เข้าไปยังโฟลเดอร์ที่เก็บไฟล์ไว้    
        3.2 Run Publisher Program ผ่านคำสั่ง 'Python3 Publisher.py'
        3.3 พิมพ์คำสั่งตาม Format ทืี่กำหนดในโปรแกรม 'Publish <broker_ip_address> <topic_name> <data_to_publish>'
        3.4 ผู้ใช้สามารถ Publish ข้อมูลได้เรื่อย ๆ จนกว่าจะทำการจบโปรแกรม 
        3.5 ผู้ใช้สามารถจบโปรแกรมได้โดยการพิมพ์ Quit หรือ Ctrl+C หรือทำการปิดหน้าต่าง Terminal

 Windows
    == วิธี run ผ่าน python interface(shell) ==
    1. Broker Program
        1.1. เปิด IDLE ของ python ขึ้นมา
        1.2. คลิก file > open ที่แถบเมนูด้านบน จากนั้นเลือกไฟล์ broker.py
        1.3. จะมีหน้าต่าง broker.py เพิ่มขึ้นมา กด f5 หรือปุ่ม run บนแถบเมนูด้านบนเพื่อทำการ run
        1.4. Broker จะถูก run และแสดง Broker IP ในหน้า Python Shell
        1.5. หากต้องการ disconnect คลิก Shell > Restart Shell บนแถบเมนูด้านบน หรือกดปุ่ม Ctrl+f6 หรือ ปิดหน้าต่างลง
    2. Subscriber Program
        2.1. เปิด IDLE ของ python ขึ้นมาใหม่
        2.2. คลิก file > open ที่แถบเมนูด้านบน จากนั้นเลือกไฟล์ subscriber.py
        2.3. จะมีหน้าต่าง subscriber.py เพิ่มขึ้นมา กด f5 หรือปุ่ม run บนแถบเมนูด้านบนเพื่อทำการ run
        2.4. Subscriber จะถูก run และแสดงผลในหน้า Python Shell
        2.5. พิมพ์ command ที่ต้องการ เช่น subscribe 127.0.0.1 '/room1/light' จากนั้นกด enter เพื่อส่งข้อมูล
        2.6. หากต้องการ disconnect คลิก Shell > Restart Shell บนแถบเมนูด้านบน หรือกดปุ่ม Ctrl+f6 หรือ ปิดหน้าต่างลง
    3. Publisher Program
        3.1. เปิด IDLE ของ python ขึ้นมาใหม่
        3.2. คลิก file > open ที่แถบเมนูด้านบน จากนั้นเลือกไฟล์ publisher.py
        3.3. จะมีหน้าต่าง publisher.py เพิ่มขึ้นมา กด f5 หรือปุ่ม run บนแถบเมนูด้านบนเพื่อทำการ run
        3.4. Publisher จะถูก run และแสดงผลในหน้า Python Shell
        3.5. พิมพ์ command ที่ต้องการ เช่น publish 127.0.0.1 '/room1/light' 'value=on' จากนั้นกด enter เพื่อส่งข้อมูล
        3.6. หากต้องการ disconnect พิม quit แล้วกด enter หรือคลิก Shell > Restart Shell บนแถบเมนูด้านบน หรือกดปุ่ม Ctrl+f6 หรือ ปิดหน้าต่างลง

    หมายเหตุ :
        - Broker สามารถรองรับ Connection ได้มากสุด 5 Connection 
        - ผู้ใช้สามารถรันโปรแกรม Publisher และ Publish ข้อมูลก่อนที่จะทำการ Subscribe ได้ 
          แต่ผู้ใช้ที่ Subscribe ที่หลังจะได้ไม่รับข้อมูลที่ทำการ Publish ก่อนหน้า
        - ควรใช้ Python3 เพื่อไม่เกิด SyntaxError 
