# DRF: Django Rest Framework

This repo is implementation of DRF consepts throuhg the Mongard course. In my journary I learned importance of DRF and Restful API,permitions, serializers, and athentication by JWT. 

## Question/Answer API

At first API for registering and creating token implemented, after creating models for Q/A, by `ModelSerializer`, **CRUD** methods was implemented.
Permisions is handled based on Token Authentication and for more control custom permission file is written.
CRUD for user model created by ViewSets.
we used **jwt** token by `djangorestframework_siimplejwt` library.
for better documentaion, we also prepear **swagger** and it is accecable at: .../schema/swager-ui .

## Requirments
```
asgiref==3.6.0
attrs==22.2.0
Django==4.1.7
djangorestframework==3.14.0
djangorestframework-simplejwt==5.2.2
drf-spectacular==0.26.1
inflection==0.5.1
jsonschema==4.17.3
PyJWT==2.6.0
pyrsistent==0.19.3
pytz==2023.3
PyYAML==6.0
sqlparse==0.4.3
tzdata==2023.3
uritemplate==4.1.1
```
