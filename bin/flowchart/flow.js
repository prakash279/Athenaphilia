const markdownText = document.getElementById('markdown-text');
const flowchartContainer = document.getElementById('flowchart-container');

// Improved parsing function:
function parseMarkdown(text) {
    const lines = text.split('\n');
    const nodes = [];
    let parentIndex = -1; // Track current parent node

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i].trim();

        // Determine node level based on header levels (more robust):
        let level = 1; // Default to level 1 for non-headers
        const match = line.match(/^#+/);
        if (match) {
            level = match[0].length;
        }

        // Handle different levels appropriately:
        if (level <= 1) { // Root node or end (empty line)
            parentIndex = -1;
        } else if (level === parentIndex + 1) { // Child of previous node
            parentIndex++;
        } else if (level > parentIndex + 1) { // Intermediate level (create intermediate parent nodes)
            for (let j = parentIndex + 1; j < level; j++) {
                nodes.push({
                    level: j,
                    text: '', // Blank content for intermediate nodes
                    children: [],
                });
            }
            parentIndex = level - 1;
        } else { // Incorrect level structure (handle as appropriate)
            console.warn(`Invalid level nesting at line ${i + 1}: ${line}`);
            // You can choose to ignore invalid lines, create warnings, etc.
        }

        nodes[parentIndex] = nodes[parentIndex] || { level, text: line, children: [] };
    }

    return nodes;
}

function createFlowchart(nodes) {
    // Clear existing flowchart (if any)
    flowchartContainer.innerHTML = '';

    // Use a suitable library or custom logic to visualize the nodes and connectors
    // Here's an example using Mermaid with basic styling:
    const flowchartText = mermaid.ganttConfig.draw([
        graph LR
        A[Start] --> B(Level 1)
        B --> C(Level 2)
        C --> D(Level 2)
        B --> E[End]
        style A, B, C, D, E
            shape square
            fill #f9f9f9
            stroke #333
            padding 10px;
        style A
            stroke-width 3px;
        style E
            stroke-width 2px;
        linkStyle
            stroke #333
            stroke-width 2px;
    ]);

    // Render the flowchart using a suitable library (e.g., Mermaid)
    mermaid.initialize({ loading: (diagram) => {
        diagram.container.classList.add('mermaid-loading');
    }, loaded: (diagram) => {
        diagram.container.classList.remove('mermaid-loading');
    } });
    flowchartContainer.innerHTML = flowchartText;
}

markdownText.addEventListener('input', () => {
    const parsedNodes = parseMarkdown(markdownText.value);
    createFlowchart(parsedNodes);
});

// Create an initial flowchart on page load:
markdownText.dispatchEvent(new Event('input'));
