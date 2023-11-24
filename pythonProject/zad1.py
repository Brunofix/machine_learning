def total_euro(radni_sati, po_satu):
return radni_sati*po_satu

radni_sati=float(input("radni sati:"))
po_satu=float(input("satnica:"))

print ("Ukupno: %d "
       "eura" % total_euro(radni_sati, po_satu))