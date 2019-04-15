# 1.Correct Model Naming  
It is generally recommended to use singular nouns for model naming, for example: User, Post, Article. That is, the last component of the name should be a noun, e.g.: Some New Shiny Item. It is correct to use singular numbers when one unit of a model does not contain information about several objects.  

# 2.Relationship Field Naming  
For relationships such as ForeignKey, OneToOneKey, ManyToMany it is sometimes better to specify a name. Imagine there is a model called Article, - in which one of the relationships is ForeignKey for model User. If this field contains information about the author of the article, then author will be a more appropriate name than user.  

# 3.Correct Related-Name  
It is reasonable to indicate a related-name in plural as related-name addressing returns queryset. Please, do set adequate related-names. In the majority of cases, the name of the model in plural will be just right. For example:  
```  
class Owner(models.Model):
    pass
class Item(models.Model):
    owner = models.ForeignKey(Owner, related_name='items')
```  

# 4.Do not use ForeignKey with unique=True  
There is no point in using ForeignKey with unique=Trueas there exists OneToOneField for such cases.  

# 5.Attributes and Methods Order in a Model  
Preferable attributes and methods order in a model (an empty string between the points).  

* constants (for choices and other)
* fields of the model
* custom manager indication
* meta
* def __unicode__ (python 2) or def __str__ (python 3)
* other special methods
* def clean
* def save
* def get_absolut_url
* other methods  
Please note that the given order was taken from documentations and slightly expanded.  

# 6.Adding a Model via Migration  
If you need to add a model, then, having created a class of a model, execute serially manage.py commands makemigrations and migrate (or use South for Django 1.6 and below).  

# 7.Denormalisations  
You should not allow thoughtless use of denormalization in relational databases. Always try to avoid it, except for the cases when you denormalise data consciously for whatever the reason may be (e.g. productivity). If at the stage of database designing you understand that you need to denormalise much of the data, a good option could be the use of NoSQL. However, if most of data does not require denormalisation, which cannot be avoided, think about a relational base with JsonField to store some data.  

# 8.BooleanField  
Do not use null=True or blank=True for BooleanField. It should also be pointed out that it is better to specify default values for such fields. If you realise that the field can remain empty, you need NullBooleanField.  

# 9.Business Logic in Models  
The best place to allocate business logic for your project is in models, namely method models and model manager. It is possible that method models can only provoke some methods/functions. If it is inconvenient or impossible to allocate logic in models, you need to replace its forms or serializers in tasks.  

# 10.
