# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：stusystem.py 
@Author  ：zero 
@Date    ：2023/4/15 22:11  
"""
import os.path

filename= 'student.txt'
def main():
    while True:
        menu()
        choice=int(input('请选择你要进行的操作>：'))
        if choice==1:
            insert()
        elif choice==2:
            search()
        elif choice==3:
            delete()
        elif choice==4:
            modify()
        elif choice == 5:
            sort()
        elif choice==6:
            total()
        elif choice==7:
            show()
        elif choice==0:
            exit_value=input('是否确定要退出(y/n)?>:')
            if exit_value=='y':
                print('已退出，感谢您的使用')
                break
            else:
                continue
        else:
            print('输入错误，请重新输入')
            continue
def menu():
    print('==============================================================')
    print('------------------------学生管理系统---------------------------')
    print('\t\t\t\t\t1、录入学生信息')
    print('\t\t\t\t\t2、查询学生信息')
    print('\t\t\t\t\t3、删除学生信息')
    print('\t\t\t\t\t4、修改学生信息')
    print('\t\t\t\t\t5、对学生排序')
    print('\t\t\t\t\t6、统计学生总人数')
    print('\t\t\t\t\t7、显示所有学生信息')
    print('\t\t\t\t\t0、退出系统')
    print('--------------------------------------------------------------')
def insert():
    while True:
        id=input('请输入学生id(如1001)>:')
        if not id:
            break
        name=input('请输入学生姓名>:')
        if not name:
            break
        try:
            english=int(input('请输入学生英语成绩>:'))
            chinese=int(input('请输入学生语文成绩>:'))
            math=int(input('请输入学生数学成绩>:'))
            science=int(input('请输入学生理科成绩>:'))
        except:
            print('输入出错啦，重新输入吧')
            continue
        #将录入的学生信息保存在字典中
        student = {'id':id,'name':name,'english':english,'chinese':chinese,'math':math,'science':science}
        #将学生信息添加到列表之中
        student_list=[]
        student_list.append(student)
        answer=input('是否继续添加？(y/n)>:')
        if answer=='y':
            continue
        else:
            break
    #调用save函数
    save(student_list)
    print('学生信息录入完毕！')
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    print(lst)
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
def search():
    #先判断学生表是否存在
    student_query=[]
    while True:
        if os.path.exists(filename):
            id=''
            name=''
            search_id=int(input('请输入要查找的选项(1.按学生id查找，2.按学生姓名查找)>:'))
            if search_id==1:
                id=input('请输入学生id>:')
            elif search_id==2:
                name=input('请输入学生姓名>:')
            else:
                print('输入错误请重新输入')
                continue
            with open(filename, 'r', encoding='utf-8') as rfile:
                student_old = rfile.readlines()
                for item in student_old:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            student_query.append(d)
                        else:
                            print('暂无该学生信息')
                    elif name!='':
                        if d['name']==name:
                            student_query.append(d)
                        else:
                            print('暂无该学生信息')
            #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer=input('是否继续查询(y/n)?>:')
            if answer=='y':
                continue
            else:
                break
        else:
            print('学生信息表为空')
            return
def show_student(lst):
    if lst==0:
        print('学生信息表中暂无数据')
        return
    else:
        #定义标题显示格式
        foemat_title='{:6}\t{:12}\t{:8}\t{:10}\t{:10}\t{:10}\t{:8}\t'
        print(foemat_title.format('ID','姓名','英语成绩','语文成绩','数学成绩','理科成绩','总分'))
        #定义类容
        foemat_data = '{:6}\t{:8}\t{:8}\t{:8}\t{:12}\t{:12}\t{:11}\t'
        for item in lst:
            print(foemat_data.format(item.get('id'),
                                     item.get('name'),
                                     item.get('english'),
                                     item.get('chinese'),
                                     item.get('math'),
                                     item.get('science'),
                                     item.get('english')+item.get('chinese')+item.get('math')+item.get('science')
                                     ))
def delete():
    while True:
        dele_id=input('请输入你要删除的学生id>:')
        if  dele_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))
                        if d['id']!=dele_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag==True:
                        print(f'删除成功id为{dele_id}的学生')
                    else:
                        print(f'没有找到id为{dele_id}的学生')
        else:
            print('无学生信息')
            break
        #删除之后要重新显示一遍所有学生信息
        answer=input('是否继续删除(y/n)?>:')
        if answer=='y':
            continue
        else:
            break
def modify():
    show()
    while True:
        #判断学生信息表文件是否存在
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as rfile:
                student_old = rfile.readlines()
        else:
            print('学生信息表为空')
            return
        modify_id = input('请输入你要修改的学生id>:')

        with open(filename, 'w', encoding='utf-8') as wfile:
            for item in student_old:
                d = dict(eval(item))
                if d['id'] == modify_id:
                    print('找到学生信息，可以进行修改了')
                    while True:
                        try:
                            d['english'] = int(input('请输入要修改的英语成绩>:'))
                            d['chinese'] = int(input('请输入要修改的语文成绩>:'))
                            d['math'] = int(input('请输入要修改的数学成绩>:'))
                            d['science'] = int(input('请输入要修改的理科成绩>:'))
                        except:
                            print('输入错误，请重新输入')
                        else:
                            break
                    wfile.write(str(d)+'\n')
                    print('修改成功！')
                else:
                    wfile.write(str(d)+'\n')
        answer=input('是否要继续修改(y/n)?>:')
        if answer=='y':
            modify()
        else:
            break
def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        student_new=[]
        for item in student_list:
            d=dict(eval(item))
            student_new.append(d)

    else:
        print('暂无学生表文件')
        return
    asc_or_desc=input('请选择(0.升序 1.降序)')
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool = True
    else:
        print('输入错误，请重新输入')
        sort()
    mode=input('请选择排序方式(1.按英语成绩 2.按语文成绩 3.按数学成绩 4.按理科成绩 5.按总成绩)\n>:')
    if mode=='1':
        student_new.sort(key=lambda x:int(x['english']),reverse=asc_or_desc_bool)
    elif mode=='2':
        student_new.sort(key=lambda x:int(x['chinese']),reverse=asc_or_desc_bool)
    elif mode=='3':
        student_new.sort(key=lambda x:int(x['math']),reverse=asc_or_desc_bool)
    elif mode=='4':
        student_new.sort(key=lambda x:int(x['science']),reverse=asc_or_desc_bool)
    elif mode=='5':
        student_new.sort(key=lambda x:int(x['enlish'])+int(x['chinese'])+int(x['math'])+int(x['science']),reverse=asc_or_desc_bool)
    else:
        print('输入错误！')
        sort()
    show_student(student_new)
def total():
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                if student:
                    print(f'一共有{len(student)}名学生')
                else:
                    print('暂无录入的学生信息')
        else:
            print('暂无学生表文件')
def show():
    student_lst=[]
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            for item in student:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
            else:
                print('学生信息表为空')

    else:
            print('暂无学生表文件')
if __name__=="__main__":
    main()
