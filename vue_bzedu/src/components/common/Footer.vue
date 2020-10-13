<template>
    <div class="footer" >
        <ul>
            <li v-for="(banner, key) in lists" :key="key"><span v-if="banner.position===2&&banner.is_site===true"><a id="a" :href="banner.link">{{banner.title}}</a></span></li>
        </ul>

    </div>
</template>

<script>
    export default {
        name: "Footer",
        data(){
            return{
                lists:[],
            }
        },
        methods:{
            alldatas(){
                this.$axios({
                    url:this.$settings.HOST+'home/navcom/',
                    method:'get',
                }).then(bt=>{
                    this.lists=bt.data
                }).catch(error=>{
                    this.$message('有错')

                })
            },
        },
        created() {
            this.alldatas()
        }
    }
</script>

<style scoped>
    .footer {
        width: 100%;
        height: 128px;
        background: #25292e;
        color: #fff;
    }

    .footer ul {
        margin: 0 auto 16px;
        padding-top: 38px;
        width: 810px;
    }

    .footer ul li {
        float: left;
        width: 112px;
        margin: 0 10px;
        text-align: center;
        font-size: 14px;
    }

    .footer ul::after {
        content: "";
        display: block;
        clear: both;
    }

    .footer p {
        text-align: center;
        font-size: 12px;
    }
    a{
        color: aliceblue;
    }
</style>
