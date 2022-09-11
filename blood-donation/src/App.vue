<template>
  <button @click="deselectRows">deselect rows</button>
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
    };
    const rowData = reactive({
      value: [
        {}
      ],
    });
    const columnDefs = reactive({
      value: [{ field: "DateDonation" }, { field: "FromHour" }, { field: "ToHour" }, { field: "Name" }, { field: "City" }, { field: "Street" }],
    });
    const defaultColDef = {
      sortable: true,
      filter: true,
    };
    onMounted(() => {
      fetch("https://d6ebtk.deta.dev/api/get-data", {})
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
      deselectRows: () =>{
        gridApi.value.deselectAll()
      }
    };
  },
};
</script>

<style lang="scss"></style>
