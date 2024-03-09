from rest_framework import serializers
from quickstart.models import Farmer, Crop, Earnings

# class FarmerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Farmer
#         fields = '__all__'

# class CropSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Crop
#         fields = '__all__'

# class EarningsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Earnings
#         fields = '__all__'


class EarningsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earnings
        fields = '__all__'

class CropSerializer(serializers.ModelSerializer):
    earnings = EarningsSerializer(many=True, read_only=True)

    class Meta:
        model = Crop
        fields = '__all__'

class FarmerSerializer(serializers.ModelSerializer):
    crops = CropSerializer(many=True, read_only=True)

    class Meta:
        model = Farmer
        fields = '__all__'
