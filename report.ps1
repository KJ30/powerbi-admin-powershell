#Log into Power BI Account 
#Login-powerbiserviceaccount

# Pull Reports

$report_csv = "powerBI_Reports.csv"
$Reports = Get-PowerBIReport -Scope Organization
$Reports | Export-Csv $report_csv
