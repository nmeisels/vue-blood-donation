<template>
  <ag-grid-vue
      class="ag-theme-alpine"
      style="height: 500px"
      :columnDefs="columnDefs.value"
      :rowData="rowData.value"
      :defaultColDef="defaultColDef"
      rowSelection="multiple"
      animateRows="true"
      @cell-clicked="cellWasClicked"
      @grid-ready="onGridReady"
  >
  </ag-grid-vue>
</template>

<script>
import { AgGridVue } from "ag-grid-vue3";
import { reactive, onMounted, ref } from "vue";
import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-alpine.css";
export default {
  name: "App",
  components: {
    AgGridVue,
  },
  setup() {
    const gridApi = ref(null);
    const onGridReady = (params) => {
      gridApi.value = params.api;
      gridApi.value.sizeColumnsToFit();
    };
    const rowData = reactive({
      value: [
        {}
      ],
    });
    const columnDefs = reactive({
      value: [{ field: "DateDonation", filter:'agDateColumnFilter', filterParams:{
          comparator: function (dataFromFilter, cellValue) {

            // dates are stored as yyyy-mm-ddThh:mm:ss
            // We create a Date object for comparison against the filter date
            const dateParts  = cellValue.split("-");

            const year = Number(dateParts[0]);
            const month = Number(dateParts[1]) - 1;
            const day = Number(dateParts[2].split("T")[0]);
            const cellDate = new Date(year, month, day);
            // Now that both parameters are Date objects, we can compare
            if (cellDate < dataFromFilter) {
              return -1;
            } else if (cellDate > dataFromFilter) {
              return 1;
            } else {
              return 0;
            }
          }
        }},
              { field: "FromHour" },
              { field: "ToHour" },
              { field: "Name" },
              { field: "City" },
              { field: "Street" },
              {field: "NumHouse"}],
    });
    const defaultColDef = reactive({
      sortable: true,
      filter: true,
      flex: 1,
      filterParams: {buttons: ["clear"]},
      floatingFilter: true,
      resizable: true
    });
    onMounted(() => {
      fetch("https://vueblood-1-c9171200.deta.app/api/get-data", {})
      .then((result) => result.json())
      .then((remoteRowData) => (rowData.value = remoteRowData));
    });
    return {
      onGridReady,
      columnDefs,
      rowData,
      defaultColDef,
      cellWasClicked: (event) => {
        console.log("cell was clicked", event);
      },
    };
  },
};
</script>

<style lang="scss"></style>
