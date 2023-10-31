function extractHTML(node) {
    // Moss @ https://stackoverflow.com/a/69867759/697964
    if (!node) return ''
    if (node.nodeType === Node.TEXT_NODE) return node.textContent.trim()
    if (node.nodeType !== Node.ELEMENT_NODE) return ''

    let html = ''
    let outer = node.cloneNode()

    // if the node has a shadowroot, jump into it
    node = node.shadowRoot || node

    if (node.children.length) {
        // we checked for children but now iterate over childNodes
        // which includes #text nodes (and even other things)
        for (let n of node.childNodes) {

            // if the node is a slot
            if (n.assignedNodes) {

                // an assigned slot
                if (n.assignedNodes()[0]) {
                    // Can there be more than 1 assigned node??
                    html += extractHTML(n.assignedNodes()[0])

                    // an unassigned slot
                } else { html += n.innerHTML }

                // node is not a slot, recurse
            } else { html += extractHTML(n) }
        }

        // node has no children
    } else {
        html = node.innerHTML
    }

    // insert all the (children's) innerHTML
    // into the (cloned) parent element
    // and return the whole package
    outer.innerHTML = html
    return outer.outerHTML
};
extractHTML(document.body)
