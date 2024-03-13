
function change() {
    let current = document.getElementById('selectonemethod').value;
    if (current === 'DELETE') {
        document.getElementById('auth').style.display = 'none';
        document.getElementById('up&down').style.display = 'none';
        document.getElementById('converter').style.display = 'none';
        document.getElementById('authorization').style.display = 'none';
        document.getElementById('sendmail').style.display = 'none';
        document.getElementById('savedata').style.display = 'none';
        document.getElementById('sendfiles').style.display = 'none';
        document.getElementById('textdelete').style.display = 'block';
        document.getElementById('trashdata').style.display = 'block';
        document.getElementById('trashfiles').style.display = 'block';
        document.getElementById('trashaccount').style.display = 'block';

    } else if (current === 'POST') {
        document.getElementById('auth').style.display = 'block';
        document.getElementById('up&down').style.display = 'block';
        document.getElementById('converter').style.display = 'block';
        document.getElementById('authorization').style.display = 'block';
        document.getElementById('sendmail').style.display = 'block';
        document.getElementById('savedata').style.display = 'block';
        document.getElementById('sendfiles').style.display = 'block';
        document.getElementById('textdelete').style.display = 'none';
        document.getElementById('trashdata').style.display = 'none';
        document.getElementById('trashfiles').style.display = 'none';
        document.getElementById('trashaccount').style.display = 'none';
    } else {
        document.getElementById('auth').style.display = 'none';
        document.getElementById('up&down').style.display = 'none';
        document.getElementById('converter').style.display = 'none';
        document.getElementById('authorization').style.display = 'none';
        document.getElementById('sendmail').style.display = 'none';
        document.getElementById('savedata').style.display = 'none';
        document.getElementById('sendfiles').style.display = 'none';
        document.getElementById('textdelete').style.display = 'none';
        document.getElementById('trashdata').style.display = 'none';
        document.getElementById('trashfiles').style.display = 'none';
        document.getElementById('trashaccount').style.display = 'none';
    }
};


