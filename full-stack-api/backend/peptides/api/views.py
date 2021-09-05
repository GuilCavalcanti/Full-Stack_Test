from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.response import Response

from peptides.api.serializers import UserSerializer, PeptideSerializer, AssaySerializer
from peptides.models import Peptide, Assay


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = None


class PeptideViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows peptides to be viewed.
    """
    queryset = Peptide.objects.all()
    serializer_class = PeptideSerializer
    pagination_class = None


class AssayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows assays to be viewed or edited.
    """
    queryset = Assay.objects.all()
    serializer_class = AssaySerializer
    pagination_class = None

    @staticmethod
    def parse_data(data):
        peptides = data.get("peptides", [])
        del data["peptides"]

        return {
            "data": data,
            "peptides": peptides,
        }

    def create(self, request, *args, **kwargs):
        parsed_data = self.parse_data(request.data)

        serializer = AssaySerializer(data=parsed_data["data"])
        serializer.is_valid(raise_exception=True)
        assay = serializer.save()

        # Excercise 2 ADD-CODE-HERE
        # Function to check if peptide name is not already in use
        def peptide_name_check(pep_name):
            if Peptide.objects.filter(name=pep_name).exists():
                return True
            return False

        for sequence in parsed_data['peptides']:
            if sequence:
                try:
                    # Check if peptide exists in the database
                    peptide = Peptide.objects.get(sequence=sequence)
                except:
                    # If it doesn't exist, create new peptide
                    number = 0
                    peptide_name = f'pep_{number}'
                    # Check if Peptide Name is not already in use
                    while peptide_name_check(peptide_name):
                        number += 1
                        peptide_name = f'pep_{number}'
                    peptide = Peptide(sequence=sequence, name=peptide_name)
                    # Save peptide
                    peptide.save()

                # Add peptide to 'many to many' peptides field
                assay.peptides.add(peptide)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
