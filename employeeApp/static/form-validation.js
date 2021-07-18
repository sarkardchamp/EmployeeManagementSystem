function validateLogin() {
    var flash = document.getElementById('flash');
    flash.innerText = '';
    var em_un, pwd;
    em_un = document.getElementById('em_un').value;
    pwd = document.getElementById('password').value;
    if (em_un.length < 1 || pwd.length < 1) {
        flash.innerText = 'All fields are required';
        return false;
    }
    return true;
}

function validateRegistration() {
    return true;
}

function validateEmpForm() {
    return true;
}

function checkPasswords() {
    var flash = document.getElementById('flash');
    flash.innerText = '';
    var oldpass, pass, cnfpass;
    oldpass = document.getElementById('oldpass').value;
    pass = document.getElementById('pass').value;
    cnfpass = document.getElementById('newpass').value;
    if (oldpass.length < 1 || pass.length < 1 || cnfpass.length < 1) {
        flash.innerText = 'All fields are required.';
        console.log('Empty field');
        return false;
    }
    if (pass != cnfpass) {
        flash.innerText = 'New Password and Confirm Password do not match.';
        console.log('Password Mismatch');
        return false;
    }
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