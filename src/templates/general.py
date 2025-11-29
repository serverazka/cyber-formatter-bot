from datetime import datetime

def general_template(data):
    """Template untuk data general"""
    table = format_data_as_table(data)
    
    return f"""
================================
        FORMAL DOCUMENT
================================

[ INFORMATION ]
{table}
[ METADATA ]
Generated : {datetime.now().strftime("%Y-%m-%d %H:%M")}
Document ID: DOC-{int(datetime.now().timestamp())}

================================
"""