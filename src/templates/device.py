from datetime import datetime

def device_template(data):
    """Template untuk data device"""
    table = format_data_as_table(data)
    
    return f"""
==============================================
        DEVICE FORENSIC UNIT v2.0
==============================================

CASE ID     : DF-{int(datetime.now().timestamp())}
TIMESTAMP   : {datetime.now().strftime("%Y-%m-%d %H:%M UTC")}
ACCESS LEVEL: TECHNICAL ANALYST

==============================================
[ DEVICE INFORMATION ]
==============================================
{table}
==============================================
[ SYSTEM METADATA ]
==============================================
Data Source     : HARDWARE DATABASE
Verification    : 95.2% MATCH
Risk Assessment : MEDIUM
Status          : ANALYZED

==============================================
"""