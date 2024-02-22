//Log into Power BI Account 

Login-powerbiserviceaccount

//Workspaces and Users

$workspace_csv = "powerBI_Workspaces.csv"
$ActiveWorkspaces = Get-PowerBIWorkspace -Scope Organization -all | Where {($_.State -eq "Active")}
$ActiveWorkspacesUsers = $ActiveWorkspaces | Select-Object ID,Name,Type,State,IsReadOnly,IsOrphaned,IsOnDedicatedCapacity,CapacityId,@{n="Users";e={$_.Users.Identifier  -join ', '}},@{n="AccessRight";e={$_.Users.AccessRight -join ', '}}
$ActiveWorkspacesUsers | Export-Csv $workspace_csv
