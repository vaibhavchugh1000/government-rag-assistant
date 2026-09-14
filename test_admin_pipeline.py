from source_code.admin_pipeline import process_document

document_path="C:\\Users\\ADMIN\\OneDrive\\Documents\\College\\Sem-7\\subjects\\NLP\\NLP Project\\source_code\\data\\documents\\doc202112201.pdf"

result=process_document(document_path)

print("document : ",result["document_name"])
print()
print("chunks created : ",result["chunks_created"])


