"""
MIT License
Copyright (c) 2017 Mackenzie Wangenstein, Chitra Maruthavanan, Andy Mayer


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from rest_framework import serializers
from website.models import Organization, Service, Testimony
from django.contrib.auth.models import User

#later change model to point to user model once it gets re-introduced
class UserSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(many=True, queryset=Service.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'services', 'organizations')

class OrganizationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Organization
    creator = serializers.ReadOnlyField(source='creator.username')
    fields = ('id', 'name', 'description', 'address', 'pub_date', 'hours_open', 'hours_close', 'creator')

  def create(self, validated_data):
    """
       Create and return a new `Organization` instance, given the validated data.
    """
    return Organization.objects.create(**validated_data)

  def update(self, instance, validated_data):
    """
        update and return an existing `Organization` instance, given the validated data.
    """
    instance.name = validated_data.get('name', instance.name)
    instance.description = validated_data.get('description', instance.description)
    instance.address = validated_data.get('address', instance.address)
    instance.pub_date = validated_data.get('pub_date', instance.pub_date)
    instance.updated_date = validated_data.get('updated_date', instance.updated_date)
    instance.hours_open = validated_data.get('hours_open', instance.hours_open)
    instance.hours_close = validated_data.get('hours_close', instance.hours_close)
    instance.save()
    return instance



class ServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Service
    creator = serializers.ReadOnlyField(source='creator.username')
    fields = ('id', 'name', 'organization', 'description', 'address', 'pub_date', 'hours_open', 'hours_close', 'creator')

  def create(self, validated_data):
    """
       Create and return a new `Organization` instance, given the validated data.
    """
    return Service.objects.create(**validated_data)

  def update(self, instance, validated_data):
    """
        update and return an existing `Organization` instance, given the validated data.
    """
    instance.name = validated_data.get('name', instance.name)
    instance.organization = validated_data.get('organization', instance.organization)
    instance.description = validated_data.get('description', instance.description)
    instance.address = validated_data.get('address', instance.address)
    instance.pub_date = validated_data.get('pub_date', instance.pub_date)
    instance.updated_date = validated_data.get('updated_date', instance.updated_date)
    instance.hours_open = validated_data.get('hours_open', instance.hours_open)
    instance.hours_close = validated_data.get('hours_close', instance.hours_close)
    instance.save()
    return instance

class TestimonySerializer(serializers.ModelSerializer):
  class Meta:
    model = Testimony
    creator = serializers.ReadOnlyField(source='creator.username')
    fields = ('id', 'title', 'story', 'author', 'creator')

  def create(self, validated_data):
    """
       Create and return a new `Organization` instance, given the validated data.
    """
    return Testimony.objects.create(**validated_data)

  def update(self, instance, validated_data):
    """
        update and return an existing `Organization` instance, given the validated data.
    """
    instance.title = validated_data.get('title', instance.title)
    instance.author = validated_data.get('author', instance.author)
    instance.story = validated_data.get('story', instance.story)
    instance.save()
    return instance
