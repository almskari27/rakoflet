from flet import *
import sqlite3

conn = sqlite3.connect("date.db",check_same_thread=False)
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    stdname TEXT,
    stdmail TEXT,
    stdphone TEXT,
    stdaddress TEXT,
    stmathmatic INTEGER,
    starabic INTEGER,
    stfrance INTEGER,
    stenglish INTEGER,
    stdrawing INTEGER,
    stchemistry INTEGER
   
)""")
conn.commit()


def main(page:Page):
    page.title='abdullah'
    page.scroll='auto'
    page.window.top= 1
    page.window.left=960
    page.window.width=390
    page.window.height=740
    page.bgcolor='white'
    page.theme_mode=ThemeMode.LIGHT

 ########################برمجة حقل الاضافة######################
    tabe_name='student'
    query =f'SELECT COUNT(*) FROM {tabe_name} '
    cursor.execute(query)
    result=cursor.fetchone()
    row_count=result[0]


 ########################برمجة حقل  الاضافة######################


 ########################حقل الاضافة######################



    def add(e):
       cursor.execute("INSERT INTO student (stdname,stdmail,stdphone,stdaddress,stmathmatic,starabic,stfrance,stenglish,stdrawing,stchemistry)VALUES(?,?,?,?,?,?,?,?,?,?)",(tname.value,tmail.value,tphone.value,taddress.value,mathmatic.value,arabic.value,france.value,english.value,draw.value,chemistry.value))
       conn.commit()              

  ########################نهاية حقل الاضافة######################


  ######################## عرض البيانات ######################
    def show(e):
        page.clean()
        c=conn.cursor()
        c.execute("SELECT * FROM student")
        users = c.fetchall()
        print(users)

        if not users =="":
            keys= ['id','stdname','stdmail','stdphone','stdaddress','stmathmatic','starabic','stfrance','stenglish','stdrawing','stchemistry']
            result= [dict(zip(keys,values)) for values in users]
            for x in result:
#########################برمجة جمع الدرجات#########################
                m = x['stmathmatic']
                a = x['starabic']
                f = x['stfrance']
                e = x['stenglish']
                d = x['stdrawing']
                c = x['stchemistry']

                res = m + a + f + e + d + c

                if res < 50 :
                   a=Text('😭راسب',size=19,color='red')

                if res > 50 :
                   a=Text('😍ناجح',size=19,color='green')
# تأكد من أن جميع المتغيرات أعداد صحيحة
                # m = int(m)  # أو float(m) إذا كانت القيم يمكن أن تكون عشرية
                # a = int(a)
                # f = int(f)
                # e = int(e)
                # d = int(d)
                # c = int(c)

# حساب النتيجة
                # res = m + a + f + e + d + c

# التحقق من النتيجة
                # if res < 50:
                #     a = Text('😭راسب', size=19, color='red')
                # elif res > 50:
                #    a = Text('😍ناجح', size=19, color='green')
                # else:
                #     a = Text('🎉ممتاز! لديك 50', size=19, color='blue')  # حالة إذا كانت النتيجة 50




##################################################
                page.add(
                   Card(
                    color='black',
                    content=Container(
                        content=Column([
                            ListTile(
                           leading=Icon(icons.PERSON),
                          title=Text('Name : '+ x['stdname'],color='white'),
                          subtitle=Text('student Email : '+ x['stdmail'],color='blue'),
                            ),
                             Row([
                               Text('Phone : ' + x['stdphone'],color='green'),
                               Text('Address : ' + x['stdaddress'],color='green'),
                            ],alignment=MainAxisAlignment.CENTER),

                             Row([
                               Text('رياضيات:' + str(x['stmathmatic']),color='blue'),
                               Text('عربي : ' + str(x['starabic']),color='blue'),
                               Text('فرنسي:' + str(x['stfrance']),color='blue'),
                            ],alignment=MainAxisAlignment.CENTER),
                             Row([
                                Text('انجليزي:' + str(x['stenglish']),color='blue'),
                                Text('رسم:' + str(x['stdrawing']),color='blue'),
                                Text('كيمباء:' + str(x['stchemistry']),color='blue'),
                             ],alignment=MainAxisAlignment.CENTER),

                               Row([
                                   a
                             ],alignment=MainAxisAlignment.CENTER),
                            
                            
                            
                            
                        ])
                    )
                )
                    
                
            )
                page.update()
  ######################## نهاية عرض البيانات ######################


 ########################حقل الادخال######################
    tname =TextField(label='اسم الطالب',icon=icons.PERSON,rtl=True,height=38)
    tmail =TextField(label='البريد الالكتروني',icon=icons.MAIL,rtl=True,height=38)
    tphone =TextField(label='رقم الهاتف',icon=icons.PHONE,rtl=True,height=38)
    taddress =TextField(label='العنوان',icon=icons.LOCATION_CITY,rtl=True,height=38)

    ##############################################

    ##########################الدرجات####################

    marktext= Text("Marks Student-علامات الطالب",text_align='center',weight='bold')
    mathmatic= TextField(label='الرياضيات',width=110,rtl=True,height=30)
    arabic= TextField(label='العربي',width=110,rtl=True,height=30)
    france= TextField(label='الفرنسي',width=110,rtl=True,height=30)
    english= TextField(label='الانجليزي',width=110,rtl=True,height=30)
    draw= TextField(label='الرسم',width=110,rtl=True,height=30)
    chemistry= TextField(label='كيمياء',width=110,rtl=True,height=30)

    ##############################################

    addbuttn= ElevatedButton(
        "اضافة طالب جديد",
        width=170,
        style=ButtonStyle(bgcolor='blue',color='white',padding=15),
        on_click=add
    )

    showbuttn = ElevatedButton(
        " عرض كل الطلاب ",
        width=170,
        style=ButtonStyle(bgcolor='blue',color='white',padding=15),
        on_click=show
    )





   
    page.add(
          Row([
         Image(src="coding3.gif",width=280)
            ],alignment=MainAxisAlignment.CENTER),

           Row([
         Text("تطبيق  المعلم والطالب في جيبك",size=20,font_family="Tahoma",color="black")
            ],alignment=MainAxisAlignment.CENTER),  


            
           Row([
         Text("عدد الطلبة المسجلين : ",size=20,font_family="Tahoma",color="blue"),
         Text(row_count,size=20,font_family="Tahoma",color="blue")
            ],alignment=MainAxisAlignment.CENTER,rtl=True),  
        tname,
        tmail,
        tphone,
        taddress,
        
    
          Row([
          marktext
          ],alignment=MainAxisAlignment.CENTER,rtl=True),  
          
          Row([
         mathmatic,arabic,france,
          ],alignment=MainAxisAlignment.CENTER,rtl=True),  
          

          Row([
            english,draw,chemistry,
          ],alignment=MainAxisAlignment.CENTER,rtl=True),  

          Row([
           addbuttn,showbuttn,
          ],alignment=MainAxisAlignment.CENTER,rtl=True), 
          
    )


  


    page.update()
app(main)
