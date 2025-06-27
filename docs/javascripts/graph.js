
// Run createGraph when the document is ready
document.addEventListener("DOMContentLoaded", function () {
    getData();
});

function getData() {

    // Sigma.js
    /*    const graph = new graphology.Graph();
        graph.addNode("1", { label: "Node 1", x: 0, y: 0, size: 10, color: "blue" });
        graph.addNode("2", { label: "Node 2", x: 1, y: 1, size: 20, color: "red" });
        graph.addEdge("1", "2", { size: 5, color: "purple" }); */

    graphElement = document.getElementById("graph-container");
    if (!graphElement) {
        console.error("Graph element not found");
        return;
    }

    // fetch the graph data from the JSON file
    fetch('/memex/colophon/graph.json').
        then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            createGraph(data);
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });

}


function createGraph(graphData) {

    const cy = cytoscape({
        container: graphElement,
        elements: { // list of graph elements to start with
            nodes: graphData.nodes,
            edges: graphData.edges
        },
        style: [ // the stylesheet for the graph
            {
                selector: 'node',
                style: { 'background-color': '#666', 'label': 'data(id)' }
            },
            {
                selector: 'edge',
                style: { 'width': 3, 'line-color': '#ccc', 'target-arrow-color': '#ccc',
                    'target-arrow-shape': 'triangle', 'curve-style': 'bezier' }
            }
        ],

        layout: {
            name: 'grid',
            rows: 1
        }

    });
}



    /*    const sigmaInstance = new Sigma(graph, graphElement);
    
        sigma.parsers.json(
            '/memex/colophon/graph.json',
            sigmaInstance,
            function () {
                // this below adds x, y attributes as well as size = degree of the node 
                var i, nodes = sigmaInstance.graph.nodes(), len = nodes.length;
    
                // Refresh the display:
                sigmaInstance.refresh();
    
                // ForceAtlas Layout
                sigmaInstance.startForceAtlas2();
            }
        ); */


// get property value --md-default-fg-color--light
/*const nodeColor = getComputedStyle(document.body).getPropertyValue("--md-default-fg-color--light")
const linkColor = getComputedStyle(document.body).getPropertyValue("--md-default-fg-color--lightest") */

/* force-graph 
fetch('/memex/colophon/graph.json').then(res => res.json()).then(data => {
      const elem = document.getElementById('graph');

// force-graph 
const Graph = new ForceGraph(elem)
        .nodeColor("white")
        .linkColor("red")
        .nodeLabel('value')
        .width(800)
        .height(600)
        .linkDirectionalParticles(2)
        .onNodeClick( node => {
          Graph.centerAt(node.x, node.y, 1000);
          Graph.zoom(8, 2000);
        })
        .graphData(data)
    });

    */