import pandas as pd
import os
import datetime as dt

filename = 'powerBI_Workspaces.csv'
workspaceType = 'Workspace'
groupType = 'PersonalGroup'


def main():
    get_csv()
  
def get_csv():
    # Workspace Users and roles
    _WorkspaceDf = pd.read_csv(filename, skiprows=1, usecols=['Id', 'Type', 'Users', 'AccessRight'],skip_blank_lines=True)
    _WorkspaceDf = _WorkspaceDf[_WorkspaceDf.Type == workspaceType]  # filter on workspace type
    _WorkspaceDf.dropna(subset=['Users'], inplace=True)  # Drop null values

    _WorkspaceUsers = _WorkspaceDf.Users.str.split(',', expand=True).stack().reset_index(level=1, drop=True)
    _WorkspaceUsers = _WorkspaceUsers.str.replace(" ", "")  # Trim blank spaces
    _WorkspaceRoles = _WorkspaceDf.AccessRight.str.split(',', expand=True).stack().reset_index(level=1, drop=True)
    _WorkspaceRoles = _WorkspaceRoles.str.replace(" ", "")  # Trim blank spaces
    _WorkspaceId = _WorkspaceDf.Id.str.split(',', expand=True).stack().reset_index(level=1, drop=True)
    _WorkspaceType = _WorkspaceDf.Type.str.split(',', expand=True).stack().reset_index(level=1, drop=True)

    _WorkspaceData = pd.concat([_WorkspaceId, _WorkspaceType, _WorkspaceUsers, _WorkspaceRoles], axis=1,keys=['Id', 'Type', 'Users', 'AccessRight'])
    _WorkspaceData.columns = ['WorkspaceID', 'Type', 'Users', 'AccessRight']
    _WorkspaceDf.drop(['Id', 'Type', 'Users', 'AccessRight'], axis=1).join(_WorkspaceData).reset_index(drop=True)

    # Group Users and roles

    _GroupDf = pd.read_csv(filename, skiprows=1, usecols=['Id', 'Type', 'Users', 'AccessRight'], skip_blank_lines=True)
    _GroupDf = _GroupDf[_GroupDf.Type == groupType]  # filter on groups type
    _GroupDf.dropna(subset=['Users'], inplace=True)  # Drop null values

    _GroupUsers = _GroupDf.Users.str.split(',', expand=True).stack().reset_index(level=1, drop=True)
    _GroupUsers = _GroupUsers.str.replace(" ", "")  # Trim blank spaces
    _GroupRoles = _GroupDf.AccessRight.str.split(',', expand=True).stack().reset_index(level=1, drop=True)
    _GroupRoles = _GroupRoles.str.replace(" ", "")  # Trim blank spaces
    _GroupId = _GroupDf.Id.str.split(',', expand=True).stack().reset_index(level=1, drop=True)
    _GroupType = _GroupDf.Type.str.split(',', expand=True).stack().reset_index(level=1, drop=True)

    _GroupData = pd.concat([_GroupId, _GroupType, _GroupUsers, _GroupRoles], axis=1,keys=['Id', 'Type', 'Users', 'AccessRight'])
    _GroupData.columns = ['WorkspaceID', 'Type', 'Users', 'AccessRight']
    _GroupDf.drop(['Id', 'Type', 'Users', 'AccessRight'], axis=1).join(_GroupDf).reset_index(drop=True)

    # Union Workspaces and Groups

    data = pd.concat([_WorkspaceData, _GroupData])

    # Result to CSV

    data.to_csv(
        r'powerBI_users.csv',
        index=None,
        header=True)


if __name__ == '__main__':
    main()
