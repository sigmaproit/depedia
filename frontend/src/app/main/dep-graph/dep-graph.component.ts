import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import * as Highcharts from 'highcharts';
import HighchartsMore from 'highcharts/highcharts-more';
import HighchartsNetwork from 'highcharts/modules/networkgraph';
import HighchartsNoDataToDisplay from 'highcharts/modules/no-data-to-display';
import * as d3 from 'd3';
import {ApiService} from '../../shared/api.service';

@Component({
    selector: 'app-dep-graph',
    templateUrl: './dep-graph.component.html',
    styleUrls: ['./dep-graph.component.sass']
})
export class DepGraphComponent implements OnInit {
    @ViewChild('graphElement', {static: false}) graphElement: ElementRef;
    depNetwork;
    graphData;

    constructor(private apiSvc: ApiService) {

    }

    ngOnInit() {

    }

    ngAfterViewInit() {
        HighchartsMore(Highcharts);
        HighchartsNoDataToDisplay(Highcharts);
        HighchartsNetwork(Highcharts);
        this.loadGraphData();
    }

    drawGraph() {
        this.depNetwork = Highcharts.chart(this.graphElement.nativeElement, {
            chart: {
                height: 800,
                events: {
                    render: (event: any) => {
                        this.drawArrows(event.target);
                    }
                }
            },
            title: {text: 'Dependency Graph'},
            series: [{
                type: 'networkgraph',
                data: this.graphData,
                draggable: false,
                lineWidth: 6,
                dataLabels: {
                    enabled: true,
                    linkFormat: ''
                },
                marker: {
                    symbol: 'square',
                    radius: 8
                },
                link: {
                    width: 5
                },
                layoutAlgorithm: {
                    linkLength: 80
                }
            }]
        });
    }

    loadGraphData() {
        this.apiSvc.getDepGraph().then((data) => {
            this.graphData = data;
            this.drawGraph();
        });
    }

    drawArrows(chart) {
        this.defineMarker();
        for (let link of this.graphData) {
            let linkHC = chart.get(link.id);
            let linkEle = linkHC.graphic.element;
            let fromElX = linkHC.fromNode.graphic.element.getBoundingClientRect().left;
            let toElX = linkHC.toNode.graphic.element.getBoundingClientRect().left;
            let arrowId = fromElX < toElX ? 'arrow' : 'arrow-rev';
            linkEle.setAttribute('marker-start', `url(#${arrowId})`);
        }
    }

    defineMarker() {
        let marker: any = document.getElementById('arrow');
        if (marker) {
            return marker;
        }
        d3.select('defs').append('svg:marker')
            .attr('id', 'arrow')
            .attr('refX', 6)
            .attr('refY', 6)
            .attr('markerWidth', 92)
            .attr('markerHeight', 30)
            .attr('markerUnits', 'userSpaceOnUse')
            .attr('orient', 'auto')
            .append('path')
            .attr('d', 'M 80 0 92 6 80 12 83 6')
            .style('fill', 'black');

        d3.select('defs').append('svg:marker')
            .attr('id', 'arrow-rev')
            .attr('refX', 6)
            .attr('refY', 6)
            .attr('markerWidth', 92)
            .attr('markerHeight', 30)
            .attr('markerUnits', 'userSpaceOnUse')
            .attr('orient', 'auto')
            .append('path')
            .attr('d', 'M 92 0 80 6 92 12 89 6')
            .style('fill', 'black');
    }

}
