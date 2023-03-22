// This will take the noteId that we pass into the function and send a request to the delte-note endpoint
// After it gets a response from the delte-note endpoint, it will reload the window to see the updated backend and remove the deleted notes
function deleteNote(noteId) {
    fetch('delete-note', {
        method: "POST",
        body: JSON.stringify({ noteId: noteId })
    }).then((_res) => {
        window.location.href = "/"
    })
}