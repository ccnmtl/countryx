/*eslint no-unused-vars: ["error", { "varsIgnorePattern": "submitFeedback|submitResetRequest" }]*/
function clearMessages() {
    var elements = getElementsByTagAndClassName(null, 'error');
    forEach(elements,
        function(elem) {
            setStyle(elem, {'display': 'none'});
        });
    elements = getElementsByTagAndClassName(null, 'success');
    forEach(elements,
        function(elem) {
            setStyle(elem, {'display': 'none'});
        });
}
var turnId = 'turn_id';
var facultyId = 'faculty_id';

function submitFeedback(form, playerId) {
    clearMessages();
    if (form.feedback.value.length < 1) {
        /*jshint -W069 */
        var id = 'error_client_' + form[turnId].value;
        $(id).innerHTML = 'Please enter some feedback before submitting.';
        setStyle($(id), {'display': 'block'});
    } else {
        var url = 'http://' + location.hostname + ':' + location.port +
            '/sim/faculty/feedback/';
        var deferred = doXHR(
            url,
            {
                method: 'POST',
                sendContent: queryString(
                    {
                        'player_id': playerId,
                        /*jshint -W069 */
                        'turn_id': form[turnId].value,
                        'feedback': form.feedback.value,
                        'faculty_id': form[facultyId].value
                    })
            });
        deferred.addCallbacks(submitFeedbackSuccess, submitError);
    }
    return false;
}

function submitFeedbackSuccess(response) {
    var doc = JSON.parse(response.responseText, null);
    var id;
    if (doc.result === 0) {
        /*jshint -W069 */
        id = 'error_client_' + doc[turnId];
        // eslint-disable-next-line no-unsafe-innerhtml/no-unsafe-innerhtml
        $(id).innerHTML = doc.message;
        setStyle($(id), {'display': 'block'});
    } else if (doc.result === 1) {
        id = 'success_client_' + doc[turnId];
        // eslint-disable-next-line no-unsafe-innerhtml/no-unsafe-innerhtml
        $(id).innerHTML = doc.message;
        setStyle($(id), {'display': 'block'});
    }
}

function submitError(err) {
    alert(err);
}

function submitResetRequest(anchor) {
    if (!confirm('Reset deletes all player turns and moves the game ' +
                 'back to the Start state. The delete process is ' +
                 'permanent and irrevocable.\n\nAre you REALLY sure ' +
                 'you want to reset this section? ')) {
        return false;
    } else {
        var deferred = doXHR(
            anchor.href,
            {
                method: 'GET'
            });
        deferred.addCallbacks(function(response) {
            var doc = JSON.parse(response.responseText, null);
            if (doc.message) {
                alert(doc.message);
            } else {
                alert('Reset complete. Turn end dates were defaulted.' +
                      '\n\nTurn 1: ' + doc.turn1 + '\nTurn 2: ' +
                      doc.turn2 + '\nTurn 3: ' + doc.turn3);
                window.location.reload();
            }
        }, submitError);
    }
}
