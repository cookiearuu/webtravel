import datetime
import os.path
import uuid

from django.db import models
#

def get_file_path(request, filename):
    original_filename = filename
    now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # Use underscores or dashes instead of colons
    unique_filename = f"{now_time}_{uuid.uuid4().hex}_{original_filename}"  # Append a UUID for uniqueness
    return os.path.join('uploads/', unique_filename)
import os
import datetime
import re

#def get_file_path(request, filename):
    #original_filename = filename
    # Generate a unique filename using a UUID
   # unique_filename = str(uuid.uuid4())
    # Get the file extension
   # file_extension = os.path.splitext(original_filename)[1]
    # Sanitize the filename by removing invalid characters
  ##  sanitized_filename = re.sub(r'[<>:"/\\|?*]', '', original_filename)
    # Combine the unique filename, sanitized filename, and file extension
   # filename = f"{unique_filename}{sanitized_filename}{file_extension}"
   # return os.path.join('uploads/', filename)

class touragencies(models.Model):
    name=models.CharField(max_length=50,unique=True,null=False)
    BIN=models.CharField(max_length=12,unique=True,primary_key=True,null=False)
    email=models.CharField(max_length=50,null=False)
    address=models.CharField(max_length=100,null=False)
    phonenumber=models.CharField(max_length=12,unique=True,null=False)
    password=models.CharField(max_length=100,null=False)
    imagee=models.ImageField(upload_to=get_file_path,null=False,default='default_value')

    def str(self):
        return self.name

class category(models.Model):
    category_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=50, unique=True, null=False)
    image = models.ImageField(upload_to=get_file_path, null=False)
    def str(self):
        return self.name


class tours(models.Model):
    id = models.IntegerField(primary_key=True,null=False)
    place=models.CharField(max_length=100,null=False)
    transport=models.CharField(max_length=50,null=False)
    quantity=models.CharField(max_length=10,null=False)
    description=models.TextField(max_length=2000,null=False)
    image=models.ImageField(upload_to=get_file_path,null=False)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=False)
    agency=models.ForeignKey(touragencies,on_delete=models.CASCADE,default=874516)
    category=models.ForeignKey(category,on_delete=models.CASCADE,default=1)
    date = models.DateField(default=datetime.date.today)
    def str(self):
        return self.place

from django.db import models

class user(models.Model):
    email = models.EmailField(unique=True,primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class registeredusers(models.Model):
    # Add the foreign key field
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12,primary_key=True)
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4)
    expiration_date = models.DateField()
    email = models.ForeignKey('user', on_delete=models.CASCADE, default='cookiearu@gmail.com')
    tour = models.ForeignKey('tours', on_delete=models.CASCADE,default=22)  # Add the foreign key field

    def __str__(self):
        return self.name
#

class favorites(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    tour = models.ForeignKey(tours, on_delete=models.CASCADE)



class consultation(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    name = models.CharField(max_length=100,null=False,default='pohuii')
    email = models.ForeignKey(user, on_delete=models.CASCADE,default='cookiearu@gmail.com',null=False)
    subject = models.CharField(max_length=100,null=False)
    message = models.TextField()
    # Add other fields as needed

    def __str__(self):
        return self.name


class moderator(models.Model):
    email = models.EmailField(unique=True, primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
