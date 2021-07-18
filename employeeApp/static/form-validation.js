function validateLogin() {
    return true;
}

function validateRegistration() {
    return true;
}

function parseDate() {
    var node = document.getElementById('dob');
    var str = node.value;
    if (str.length != 13)
        return false;
    const months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',
    'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'};
    var mon = months[str.substr(0,3)];
    var dd = str.substr(5,2);
    var yy = str.substr(9,4);
    str = yy + '-' + mon + '-' + dd;
    node.value = str;
    return true;
}