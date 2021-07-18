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
    var fname, lname, city, email, dob;
    fname = document.getElementById('fname').value;
    lname = document.getElementById('lname').value;
    city = document.getElementById('city').value;
    email = document.getElementById('email').value;
    dob = document.getElementById('dob').value;
    flash = document.getElementById('flash');
    flash.innerText = '';
    if (!(fname && lname && city && email && dob)) {
        flash.innerText = 'All fields are required';
        return false;
    }
    return true;
}

function validateEmpForm() {
    if (! parseDate()) {
        document.getElementById('flash').innerText = 'Invalid Date';
        return false;
    }

    return true;
}



function validateLeaveRequest() {
    var ltype, sdate, edate, reason, flash;
    flash = document.getElementById('flash');
    flash.innerText = '';
    ltype = document.getElementById('leaveType').value;
    sdate = document.getElementById('sd').value;
    edate = document.getElementById('ed').value;
    if (!(ltype && sdate && edate)) {
        flash.innerText = 'All fields except Description are required.';
        return false;
    }
    if (edate < sdate) {
        flash.innerText = 'End Date must be greater than Start Date';
        return false;
    }
    return true;
}

function setMinDate() {
    var sdate, edate, yyyy,mm,dd;
    sdate = document.getElementById('sd');
    edate = document.getElementById('ed');
    d = new Date();
    yyyy = d.getFullYear();
    mm = 1 + d.getMonth();
    dd = d.getDate();
    if (mm < 10) {
        mm = '0' + mm;
    }
    if (dd < 10) {
        dd = '0' + dd;
    }
    sdate.setAttribute('min', '' + yyyy + '-' + mm + '-' + dd);
    edate.setAttribute('min', '' + yyyy + '-' + mm + '-' + dd);
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
    var mon, dd, yy;
    if (str.length > 13 || str.length < 12)
        return false;
    const months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',
    'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'};
    mon = months[str.substr(0,3)];
    if (mon == '05') {
        dd = str.substr(4,2);
        yy = str.substr(8,4);
    } else {
        dd = str.substr(5,2);
        yy = str.substr(9,4);
    }
    str = yy + '-' + mon + '-' + dd;
    console.log(str);
    if (str.length != 10) {
        return false;
    }
    node.value = str;
    return true;
}