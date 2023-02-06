from pydantic import BaseModel, constr
from datetime import date, datetime, datetime


class TypesOfLesson(BaseModel):
    '''
    Table for types of lessons. For ex., group lesson or personal lesson

    id
    name - name of lesson
    client_price - amount, that client must pay for that type of lesson
    staff_payment - amount, that staff will have for this type of lesson
    is_actual
    '''
    id : int = None
    name : constr(max_length=100)
    client_price : float = None
    staff_payment : float = None
    is_actual : bool


class Dogs(BaseModel):
    '''
    Dogs info

    staff_id - instructor's id
    place_id - default place for lesson. It helps to autofill field lessons.place_id
    '''
    id : int = None
    name : constr(max_length=20)
    breed : constr(max_length=20)
    is_learning : bool   
    staff_id : int = None
    place_id : int = None


class UserDog(BaseModel):
    '''
    Many to many table. One dog may have many owners and vice versa
    '''
    id : int = None
    staff_id : int = None
    dog_id : int = None
    

class Lessons(BaseModel):
    '''
    Table for lessons. Connects staff, dog, place, type of lesson
    '''
    id : int = None
    date : datetime  
    dog_id : int
    place_id : int
    type_of_lesson_id : int
    staff_id : int


class Staff(BaseModel):
    '''
    Information about all users (customers and staff)
    
    id
    name - person's name
    role - (-1)-3 (customer without adv/ customer with adv/ instuctor/ administrator/ sen. administrator)
    ...
    '''
    id : int = None
    name : constr(max_length=20)
    role : int
    phone : constr(max_length=15)
    date_of_birth : date = None
    tg_id : int = None
    e_mail : constr(max_length=100) = None


class Places(BaseModel):
    '''
    Information about places, where lessons run
    '''
    id : int = None
    address : constr(max_length=255)
    name : constr(max_length=30)
    is_actual : bool   


class Advertisements(BaseModel):
    '''
    Table for advertisements. Advertisements will be sended by tg or e-mail

    id
    name - name of adv (information for staff)
    created_by - staff, that created this adv
    date_to_post
    topic - for e-mail
    text
    send_to - 1/2/3 (tg/e-mail/both)
    '''
    id : int = None
    name : constr(max_length=20)
    created_by : int
    date_to_post : datetime = datetime.now()
    topic : constr(max_length=100)
    text : constr(max_length=255)
    send_to : constr(max_length=2) 
    

class Users(BaseModel):
    '''
    StaffAuth more correct name for this table. Kepps passwords for staff
    '''
    id : int = None
    password : constr(max_length=100)
    staff_id : int
    

class Courses(BaseModel):
    '''
    Information about courses, that customers may buy

    id
    name - name of course
    lesson_amount - amount of lessons, that customer may attend
    price
    is_actual
    '''
    id : int = None
    name : constr(max_length=100)
    lesson_amount : int
    price : float
    is_actual : bool


class DogCourse(BaseModel):
    '''
    Many to many table. For one dog may be bought many courses and vice versa
    '''
    id : int = None
    dog_id : int
    course_id : int
    date : date
