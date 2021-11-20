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
      <div class='service-card-item hvr-bubble-left' v-for ='service in services.templates' :key = service.id>
            <span class='active-turner'>
              {{ service.name }}
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
      searchValue: '',
      services : []
    }
  },
  mounted() {
    this.$refs.serviceTextField.focus()
    this.fetchServices()
  },
  methods: {
    search() {
      // something actions width this.searchValue
    },
    async fetchServices() {
      // this.services = await this.$axios.$get('https://rd-api.loca.lt/service')
      this.services = await this.$axios.$get('http://127.0.0.1:5000/api/services')

      for (let elem of this.services.templates) {
        console.log(elem.name)
      }

    }
  }
}

</script>
<style src='../layouts/hovers.css'></style>
