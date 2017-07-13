from rest_framework import serializers
from website.models import Organization, Shelter


class OrganizationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Organization
    fields = ('id', 'name', 'description', 'address', 'pub_date', 'hours_open', 'hours_close')

    # alternative to serializers.modelSerializer.  replace serializers. modelSerializer with
    # serializers.Serializer
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=False, allow_blank=True, max_length=200)
    # description = serializers.CharField(required=False, allow_blank=True, max_length=200)
    # address = serializers.CharField(required=False, allow_blank=True, max_length=200)
    # pub_date = serializers.DateTimeField()
    # hours_open = serializers.TimeField()
    # hours_close = serializers.TimeField()

  def create(self, validated_date):
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
    instance.hours_open = validated_data.get('hours_open', instance.hours_open)
    instance.hours_close = validated_data.get('hours_close', instance.hours_close)
    instance.save()
    return instance
