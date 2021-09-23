<template>
  <div class='md:px-10 py-5'>
    <center>
      <div class='service-container'>
        <input class='service-text-field px-5' placeholder="Поиск по услугам..." v-model='searchValue'
               @keyup.enter='search' ref='serviceTextField'>
        <img src='../static/zoom.png' class='search-zoom' @click='search'>
      </div>
      <br>
    </center>

    <div class='service-card'>
      <div class='service-card-item hvr-bubble-left'>
            <span class='active-turner'>
              Сдать анализ на COVID-19
            </span>
      </div>
    </div>

    <div class='service-card-footer'>
      <center>
          <span class='active-turner px-2 py-1'>
            helpdesk@radolyn.com
          </span>
      </center>
    </div>

  </div>
</template>

<script>

export default {
  data() {
    return {
      searchValue: ''
    }
  },
  mounted() {
    this.$refs.serviceTextField.focus()
  },
  methods: {
    search() {
      // something actions width this.searchValue
    }
  }
}

</script>
<style src='../layouts/hovers.css'></style>
