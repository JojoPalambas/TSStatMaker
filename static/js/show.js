console.log("OPEN show.js");

let tasksPersistance = null;

function dateToString(date) {
    var ret = "";

    ret += date.getFullYear().toString();
    ret += "-";

    if ((date.getMonth() + 1).toString().length === 1)
        ret += 0;
    ret += (date.getMonth() + 1).toString();
    ret += "-";

    if (date.getDate().toString().length === 1)
        ret += 0;
    ret += date.getDate().toString();

    return ret;
}

function loadChart(tasks) {
    tasksPersistance = tasks;

    google.charts.load('current', {packages: ['corechart', 'line']});
    google.charts.setOnLoadCallback(drawCurveTypes);
}

function groupTasksByDate(tasks) {
    console.log("Group tasks by date");
    const dates = [];

    let startDate = new Date(tasks[0].startDate);
    let endDate = new Date(tasks[0].startDate);

    // Finding the startDate and the endDate
    for (let i = 0; i < tasks.length; i++) {

        if (dateToString(startDate) > tasks[i].startDate)
            startDate = new Date(tasks[i].startDate);
        if (dateToString(endDate) < tasks[i].startDate)
            endDate = new Date(tasks[i].startDate);
    }

    // Building the histogram of empty dates
    let currentDate = new Date(tasks[0].startDate);
    while (dateToString(currentDate) <= dateToString(endDate)) {
        dates.push({
            date: new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate()),
            tasks: []
        });
        currentDate.setDate(currentDate.getDate() + 1);
    }

    // Putting the tasks in the histogram
    for (let i = 0; i < tasks.length; i++) {
        const index = dates.findIndex(function(date) {return dateToString(date.date) === tasks[i].startDate});
        // Checks if the date of the task is in the dates list
        if (index >= 0) {
            dates[index].tasks.push(tasks[i]);
        }
    }

    console.log(dates);
    return dates;
}

function applyGranularity(dates) {
    console.log("Apply granularity");
    const ret = [];

    console.log(ret);
    return dates;
}

function applyDateFilters(dates) {
    console.log("Apply date filters");
    const ret = [];

    console.log(ret);
    return dates;
}

function applyProjectFilter(dates) {
    console.log("Apply project filter");
    const ret = [];

    console.log(ret);
    return dates;
}

function applyTaskFilter(dates) {
    console.log("Apply task filter");
    const ret = [];

    console.log(ret);
    return dates;
}

// Converts a "X:XX:XX" duration to a number of hours
function durationToHours(duration) {
    const splitted = duration.split(":");
    return parseInt(splitted[0]) + (parseInt(splitted[1]) / 60);
}

function accumulateByDisplayMode(dates) {
    console.log("Accumulate by display mode");
    const ret = accumulateByProject(dates);

    console.log(ret);
    return ret;
}

function accumulateByProject(dates) {
    const ret = {columns: [], rows: []};

    // Listing the projects
    for (let i = 0; i < dates.length; i++) {
        for (let j = 0; j < dates[i].tasks.length; j++) {
            if (ret.columns.findIndex(function(column) {return column === dates[i].tasks[j].project}) === -1)
                ret.columns.push(dates[i].tasks[j].project);
        }
    }

    // Accumulating the times
    for (let i = 0; i < dates.length; i++) {
        const row = [dates[i].date];

        // Building the histogram
        for (let j = 0; j < ret.columns.length; j++)
            row.push(0);

        // Filling the histogram
        for (let j = 0; j < dates[i].tasks.length; j++) {
            const task = dates[i].tasks[j];
            const index = ret.columns.findIndex(function(column) {return column === task.project});

            if (index === -1 || index >= row.length - 1)
                continue;
            row[index + 1] += durationToHours(task.duration);
        }

        ret.rows.push(row);
    }

    return ret;
}

function accumulateByTask(dates) {
    const ret = [];

    return dates;
}

function drawCurveTypes() {
    // Gets the list of dates containing all the events
    let data = tasksPersistance;
    data = groupTasksByDate(data);

    // Refines the data
    data = applyGranularity(data);
    data = applyDateFilters(data);
    data = applyProjectFilter(data);
    data = applyTaskFilter(data);

    // Makes the data digest for the chart, regarding the display mode
    var columnsRows = accumulateByDisplayMode(data);

    const dataTable = new google.visualization.DataTable();

    // Adding the columns
    console.log(columnsRows);
    dataTable.addColumn('date', "Moment");
    for (let i = 0; i < columnsRows.columns.length; i++) {
        dataTable.addColumn('number', columnsRows.columns[i]);
    }

    // Adding the rows
    dataTable.addRows(columnsRows.rows);

    /*
    dataTable.addColumn('number', 'X');
    dataTable.addColumn('number', 'Dogs');
    dataTable.addColumn('number', 'Cats');

    dataTable.addRows([
        [0, 0, 0],    [1, 10, 5],   [2, 23, 15],  [3, 17, 9],   [4, 18, 10],  [5, 9, 5],
        [6, 11, 3],   [7, 27, 19],  [8, 33, 25],  [9, 40, 32],  [10, 32, 24], [11, 35, 27],
        [12, 30, 22], [13, 40, 32], [14, 42, 34], [15, 47, 39], [16, 44, 36], [17, 48, 40],
        [18, 52, 44], [19, 54, 46], [20, 42, 34], [21, 55, 47], [22, 56, 48], [23, 57, 49],
        [24, 60, 52], [25, 50, 42], [26, 52, 44], [27, 51, 43], [28, 49, 41], [29, 53, 45],
        [30, 55, 47], [31, 60, 52], [32, 61, 53], [33, 59, 51], [34, 62, 54], [35, 65, 57],
        [36, 62, 54], [37, 58, 50], [38, 55, 47], [39, 61, 53], [40, 64, 56], [41, 65, 57],
        [42, 63, 55], [43, 66, 58], [44, 67, 59], [45, 69, 61], [46, 69, 61], [47, 70, 62],
        [48, 72, 64], [49, 68, 60], [50, 66, 58], [51, 65, 57], [52, 67, 59], [53, 70, 62],
        [54, 71, 63], [55, 72, 64], [56, 73, 65], [57, 75, 67], [58, 70, 62], [59, 68, 60],
        [60, 64, 56], [61, 60, 52], [62, 65, 57], [63, 67, 59], [64, 68, 60], [65, 69, 61],
        [66, 70, 62], [67, 72, 64], [68, 75, 67], [69, 80, 72]
    ]);
    */

    const options = {
        height: 1000,
        hAxis: {
            title: 'Moment of the year'
        },
        vAxis: {
            title: 'Time spent'
        }};

    const chart = new google.visualization.LineChart(document.getElementById('line-chart-container'));
    chart.draw(dataTable, options);
}