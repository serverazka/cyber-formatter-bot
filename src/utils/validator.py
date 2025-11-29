import re

def clean_value(value):
    """Bersihkan value dari karakter yang tidak diinginkan"""
    if not value:
        return value
    
    value = re.sub(r'\s+', ' ', value)
    
    unwanted_patterns = [
        r'\bLengkap\s*:\s*',
        r'\bFull\s*:\s*', 
        r'\bComplete\s*:\s*',
        r'^\s*:\s*',
        r'\s*:\s*$'
    ]
    
    for pattern in unwanted_patterns:
        value = re.sub(pattern, '', value, flags=re.IGNORECASE)
    
    return value.strip()

def validate_nik(nik):
    """Validasi NIK"""
    if not nik:
        return False, "NIK tidak boleh kosong"
    
    if not re.match(r'^\d{16}$', str(nik)):
        return False, "NIK harus 16 digit angka"
    
    return True, "NIK valid"

def validate_data(data):
    """Validasi data secara keseluruhan"""
    errors = []
    
    if 'nik' in data:
        is_valid, message = validate_nik(data['nik'])
        if not is_valid:
            errors.append(message)
    
    return len(errors) == 0, errors