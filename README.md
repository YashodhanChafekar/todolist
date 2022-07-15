# todolist
This is repo for my todo-list app  (Tutorial App).
This project gives user ability to create a Todo-List. User can perform simple CRUD operations on to do list. To do list have following fields. Title, Description, Created_date, Meetlink(for online meetig link.), complete(Task done or not done).
Landing page 
![Todolist](https://user-images.githubusercontent.com/108964197/179212631-f68da49f-f398-4d97-a9ad-583894c88cc1.png)
Add Task Form:
It lets you add task and also you can specify meet link. 
![image](https://user-images.githubusercontent.com/108964197/179212731-2d734477-a2fc-4be0-bb96-e89b29298fec.png)
Here Title is CharField. Description is TextField. Created_Date is DateTimeField. Meetlink is clickable URLField. Complete is BooleanField.
App is Loginrequired. It lands user on Task list view. Generally todo list does not need to be seperated datewise( that is new list for new date). So here each task has created_date. After done you can delete task. You can edit and create task as well. I am happy if anyone can use this project as it is. Thanks for being here, and wish me luck for my future journey as developer.
For using this project as it is, you will only need a django installed on your device and nothing else. 
