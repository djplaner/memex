
// Run createGraph when the document is ready
document.addEventListener("DOMContentLoaded", function () {
    getData();
});

function getData() {
    // fetch the graph data from the JSON file
    fetch('/memex/colophon/graph.json').
    //fetch('https://assets.antv.antgroup.com/g6/graph.json').
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

function createGraph(data) {
    // Sigma.js
    //const graph = new graphology.Graph();

/*    graphElement = document.getElementById("graph-container");
    if (!graphElement) {
        console.error("Graph element not found");
        return;
    } */


    // G6
    const { Graph } = G6;

    const graph = new Graph({
        container: 'graph-container',
        autoFit: 'view',
        data,
        plugins: [
            {
                type: 'tooltip',
                getContent: (e,items) => {
                    const node = items[0].data;
                    return `<div class="tooltip-content">
                                <h3>${node.name}</h3>
                                <p>ID: <a href="${items[0].id}">${items[0].id}</a></p>
                            </div>`;
                }
            }
        ],
        node: {
          style: {
            size: 10,
          },
          palette: {
            field: 'group',
            color: 'tableau',
          },
        },
        layout: {
//            type: 'force-atlas2', preventOverlap: true, kr: 20, center: [250,250]
          type: 'd3-force',
          manyBody: {},
          x: {},
          y: {}, 
        },
        behaviors: ['drag-canvas', 'zoom-canvas', 'drag-element'],
      });

      graph.render();


    
//            { "id": "/pkm.md", "x": 1, "y": 1, "label": "Personal Knowledge Management" },
    // Add data['nodes'] to the graph
/*    data.nodes.forEach(node => {
        graph.addNode(node.id, {
            label: node.label || node.id, // Use node.id as label if label is not provided
            //x: node.x || Math.random(), // Use random x if not provided
            x: Math.random(), // Use random x if not provided
            //y: node.y || Math.random(), // Use random y if not provided
            y: Math.random(), // Use random y if not provided
            size: node.size || 5, // Default size to 1 if not provided
            color: node.color || '#666' // Default color to gray if not provided
        });
    }); */

    //  { "id": "1", "source": "/seek/seek.md", "target": "/pkm.md" },
    // Add data['edges'] to the graph
/*    data.edges.forEach(edge => {
        graph.addEdge(edge.source, edge.target, {
            size: edge.size || 1, // Default size to 1 if not provided
            color: edge.color || '#ccc' // Default color to light gray if not provided
        });
    }); 



    renderer = new Sigma(graph, graphElement );

    const positions = forceAtlas2( graph, {iterations:50});
    forceAtlas2.assign(graph, positions); */

    /*    graph.addNode("1", { label: "Node 1", x: 0, y: 0, size: 10, color: "blue" });
        graph.addNode("2", { label: "Node 2", x: 1, y: 1, size: 20, color: "red" });
        graph.addEdge("1", "2", { size: 5, color: "purple" }); */

/*    const cy = cytoscape({
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

    }); */
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