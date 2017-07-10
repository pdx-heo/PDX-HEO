The goal of this page is to serve as a tutorial to test the serializer in django REST framework.

To begin:
      Run ```docker-compose run testserializer```

      This will build the python env and run the command python manager.py shell

      From there enter the following commnds into the command prompt:

```     from pdxheo.models import Organization
        from pdxheo.serializers import OrganizationSerializer
        from rest_framework.renderers import JSONRenderer
        from rest_framework.parsers import JSONParser

                #get existing organization
         organization = Organization.objects.get(name='Multnomah County')

              #serialize the instance ie translate model instance into Python #native datatypes
         serializer = OrganizationSerializer(organization)
         serializer.data

              #render data into json
         content = JSONRenderer().render(serializer.data)
         content
```
