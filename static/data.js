(function () {
    $('#container').highcharts({
        title: {
            text: '金洲ME60-1 11月',
            x: -20 //center
        },
        subtitle: {
            text: '各类型带宽',
            x: -20
        },
        xAxis: {
            categories: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        },
        yAxis: {
            title: {
                text: 'second '
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: 'sec'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: '1M',
            data: [19436449, 16252044, 18562851, 15379751, 18471034, 15783701, 18143051, 16939744, 17469133, 16749748, 17308778, 16654172, 17664020, 16637586, 16974106, 16754352, 15985932, 17197762, 15085568, 14212154, 16753591, 17795531, 15530597, 18251763, 15956643, 17342404, 16017516, 18706708, 10078707, 4551573]
        }, {
            name: '2M',
            data: [184546592, 161813921, 171238126, 161231806, 168922959, 168509880, 180174114, 172579461, 173178006, 163917749, 170579468, 163641952, 165851424, 170393866, 169049298, 162405063, 166189930, 156878483, 160008355, 115707515, 179825180, 150580931, 169793267, 148157342, 168751156, 149981330, 161265806, 157488235, 90223472, 43012170]
        }, {
            name: '4M',
            data: [822945715, 724289168, 759288249, 720881766, 760099680, 729759229, 811113217, 775369553, 758165698, 740536126, 760702771, 732815725, 750699134, 766574378, 781028402, 725037538, 759539224, 707687685, 735937791, 527810623, 833364638, 677131956, 787587149, 682479713, 769497471, 677333804, 763560646, 721541482, 403226391, 165290454]
        }, {
            name: '8M',
            data: [2984464, 3941146, 4414098, 4675333, 3734233, 5216630, 3339302, 4418154, 2330710, 5277541, 3229305, 4641296, 3420642, 4800613, 2547929, 4034222, 3365714, 4115464, 3643585, 3607660, 3595001, 3984177, 2225542, 5141883, 3343644, 4595623, 3867906, 4527002, 859780, 418830]
            }, {
            name: '10M',
            data: [911893920, 767140000, 882710240, 777255752, 875910557, 807716436, 913892286, 845138705, 841401569, 824992043, 861506515, 813827023, 860627009, 857807769, 860183351, 809997682, 856063208, 796604196, 835893769, 582541105, 971384047, 706738811, 885324505, 765273271, 861798509, 751541352, 853358025, 802354804, 360097882, 138984574]
            }, {
            name: '20M',
            data: [78933960, 60945380, 77255923, 63521308, 75198500, 65158701, 78162356, 67856510, 70849912, 69070286, 73983244, 66461802, 75042487, 65709680, 75616912, 63933417, 73933891, 65444256, 72415121, 46797340, 85079925, 54849295, 74994729, 64524016, 74411120, 64628718, 71923723, 69340021, 23112510, 7870904]

        }]
    });
});
