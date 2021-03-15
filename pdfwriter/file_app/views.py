from django.shortcuts import render
from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from .models import File
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class FileView(APIView):
  # parser_classes = (MultiPartParser, FormParser)

  def post(self, request, format = None):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
    #   return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    # else:
    #   return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


      packet = io.BytesIO()
      can = canvas.Canvas(packet, pagesize=letter)
      can.drawString(295, 625, "PRASHANT SACHAN")
      can.drawString(295, 600, "MANTRA LABS GLOBAL")
      # page_two = can.drawString(100, 600, "Hello PRASHANT")
      can.save()

      packet.seek(0)
      new_pdf = PdfFileReader(packet)
      # read your existing PDF
      pdf_path = "media/upload/" + str(request.data['file'])
      pdffile = open(pdf_path, "rb")
      existing_pdf = PdfFileReader(pdffile)
      output = PdfFileWriter()
      # add the "watermark" (which is the new pdf) on the existing page
      page = existing_pdf.getPage(0)
      page.mergePage(new_pdf.getPage(0))
      output.addPage(page)
      pdfmodified_path = "./media/result/" + str(request.data['file'])
      # breakpoint()
      # finally, write "output" to a real file
      outputStream = open(pdfmodified_path, "wb")
      output.write(outputStream)
      outputStream.close()

      return Response({'msg':'data created', "data":pdfmodified_path}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
