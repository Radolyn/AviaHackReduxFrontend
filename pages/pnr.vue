<template>
  <div>
    <center>
      <div class='card'>
        <br>
        <div class='grid grid-cols-7'>
          <nuxt-link to="/cellphone" class='col-start-3'>
            <div>
              <span class='active-turner px-2 py-2'>Телефон</span>
            </div>
          </nuxt-link>
          <div class='col-start-4'>
            <div style='width : 1px; height : 30px; background : #EBD2DA'></div>
          </div>
          <div class='col-start-5'>
            <div>
              <span class='px-4 py-2'>PNR</span>
            </div>
            <img src='../static/ellipse.png' class='pnr-quest' @click='pnrShow = true'>
          </div>
        </div>
        <div v-show='pnrShow' style='border : 1px solid #EBD2DA; border-radius: 10px; width : 420px'>
          <span>
            PNR - запись в базе данных компьютерной системы бронирования о маршруте пассажира, находящаяся на посадочном талоне
          </span>
        </div>

        <br>
        <input placeholder="Ваш PNR" class='text-field' ref='pnrTextField' type='tel' v-model='pnrValue'/>

        <br><br>

        <nuxt-link to='/' style='position:relative; float : right; right : 80px'>
          <span class='active-turner px-4 py-2'>Далее</span>
        </nuxt-link>

        <br><br>

        <div class='grid' ref='questions'>
          <div class='row-start-1'><br></div>
          <div class='row-start-2'><br></div>
          <div class='row-start-3'><br></div>
          <div class='row-start-4'><br></div>
          <div class=' row-start-5'><br></div>
          <div class='row-start-6'><br></div>
          <div class=' row-start-7'><br></div>
          <div class='row-start-8'><br></div>
          <div class='row-start-9'><br></div>
          <div class='row-start-10'>
             <span>
              Есть вопросы?
            </span>
          </div>
          <div class='row-start-11'>
            <span class='active-turner px-2 py-1'>
              helpdesk@radolyn.com
            </span>
          </div>
        </div>
      </div>
    </center>
  </div>

</template>

<script>
import IMask from "imask";

export default {
  data() {
    return {
      pnrShow: false,
      pnrValue: ''
    }
  },
  mounted() {
    this.$refs.pnrTextField.focus()

    const pnrMaskOption = {
      mask: 'aaaa00'
    }
    IMask(this.$refs.pnrTextField, pnrMaskOption)
  },
  watch: {
    pnrShow() {
      let elements = this.$refs.questions

      for (let i = 0; i < elements.childNodes.length; i++) {
        elements.childNodes[i].innerHTML = '';

        if (i >= 6) {
          break
        }
      }
    },
    pnrValue() {
      this.pnrValue = this.pnrValue.toUpperCase()
    }
  }
}

</script>

<style>

.pnr-quest {
  position: relative;
  left: 15px;
  bottom: 24px;
  float: right;
  cursor: pointer;
}

</style>
