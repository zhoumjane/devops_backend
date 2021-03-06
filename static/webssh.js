function get_connect_info() {
    let host = $.trim($('#host').val());
    let port = $.trim($('#port').val());
    let user = $.trim($('#user').val());
    let current_user = $.trim($('#current_user').val());
    let remote_addr = $.trim($('#remote_addr').val());
    // let auth = $("input[name='auth']:checked").val();
    let auth = 'key';
    let pwd = $.trim($('#password').val());
    let password = window.btoa(pwd);
    let ssh_key = 'id_rsa.pub';

    // if (auth === 'key') {
    //     let pkey = $('#pkey')[0].files[0];
    //     let csrf = $("[name='csrfmiddlewaretoken']").val();
    //     let formData = new FormData();
    //
    //     formData.append('pkey', pkey);
    //     formData.append('csrfmiddlewaretoken', csrf);
    //
    //     $.ajax({
    //         url: '/upload_ssh_key/',
    //         type: 'post',
    //         data: formData,
    //         async: false,
    //         processData: false,
    //         contentType: false,
    //         mimeType: 'multipart/form-data',
    //         success: function (data) {
    //             ssh_key = data;
    //         }
    //     });
    // }

    let connect_info1 = 'host=' + host + '&port=' + port + '&user=' + user + '&auth=' + auth + '&current_user=' + current_user + '&remote_addr=' + remote_addr;
    let connect_info2 = '&password=' + password + '&ssh_key=' + ssh_key;
    let connect_info = connect_info1 + connect_info2;
    return connect_info
}


function get_term_size() {
    let init_width = 9;
    let init_height = 17;

    let windows_width = $(window).width();
    let windows_height = $(window).height();

    return {
        cols: Math.floor(windows_width / init_width),
        rows: Math.floor(windows_height / init_height),
    }
}

function websocket() {
    let cols = get_term_size().cols;
    let rows = get_term_size().rows;
    let connect_info = get_connect_info();

    let term = new Terminal(
        {
            cols: cols,
            rows: rows,
            useStyle: true,
            cursorBlink: true
        }
        ),
        protocol = (location.protocol === 'https:') ? 'wss://' : 'ws://',
        socketURL = protocol + location.hostname + ((location.port) ? (':' + location.port) : '') +
            '/webssh/?' + connect_info + '&width=' + cols + '&height=' + rows;

    let sock;
    sock = new WebSocket(socketURL);
    sock.binaryType = "arraybuffer";    // ???????????????zmodem ???????????????

    function uploadFile(zsession) {
        let uploadHtml = "<div>" +
            "<label class='upload-area' style='width:100%;text-align:center;' for='fupload'>" +
            "<input id='fupload' name='fupload' type='file' style='display:none;' multiple='true'>" +
            "<i class='fa fa-cloud-upload fa-3x'></i>" +
            "<br />" +
            "??????????????????" +
            "</label>" +
            "<br />" +
            "<span style='margin-left:5px !important;' id='fileList'></span>" +
            "</div><div class='clearfix'></div>";

        let upload_dialog = bootbox.dialog({
            message: uploadHtml,
            title: "????????????",
            buttons: {
				cancel: {
					label: '??????',
					className: 'btn-default',
					callback: function (res) {
						try {
							// zsession ??? 5s ???????????? ZACK ??????5s ???????????????????????????????????? ???ZACK??? ??????????????????
							// ?????????????????? _last_header_name ??? ZRINIT???????????????????????????
							zsession._last_header_name = "ZRINIT";
							zsession.close();
						} catch (e) {
							console.log(e);
						}
					}
				},
            },
			closeButton: false,
        });

        function hideModal() {
			upload_dialog.modal('hide');
		}

		let file_el = document.getElementById("fupload");

		return new Promise((res) => {
			file_el.onchange = function (e) {
				let files_obj = file_el.files;
				hideModal();
				Zmodem.Browser.send_files(zsession, files_obj, {
						on_offer_response(obj, xfer) {
							if (xfer) {
								// term.write("\r\n");
							} else {
								// term.write("\r\n" + obj.name + " was upload skipped");
								term.write(obj.name + " was upload skipped\r\n");
								//socket.send(JSON.stringify({ type: "ignore", data: utoa("\r\n" + obj.name + " was upload skipped\r\n") }));
							}
						},
						on_progress(obj, xfer) {
							updateProgress(xfer);
						},
						on_file_complete(obj) {
							//socket.send(JSON.stringify({ type: "ignore", data: utoa("\r\n" + obj.name + " was upload success\r\n") }));
							// console.log("COMPLETE", obj);
                            term.write("\r\n");
						},
					}
				).then(zsession.close.bind(zsession), console.error.bind(console)
				).then(() => {
					res();
					// term.write("\r\n");
				});
			};
		});
    }

	function saveFile(xfer, buffer) {
		return Zmodem.Browser.save_to_disk(buffer, xfer.get_details().name);
	}

	function updateProgress(xfer) {
		let detail = xfer.get_details();
		let name = detail.name;
		let total = detail.size;
		let percent;
		if (total === 0) {
			percent = 100
		} else {
			percent = Math.round(xfer._file_offset / total * 100);
		}

		term.write("\r" + name + ": " + total + " " + xfer._file_offset + " " + percent + "%    ");
	}

	function downloadFile(zsession) {
		zsession.on("offer", function(xfer) {
			function on_form_submit() {
				let FILE_BUFFER = [];
				xfer.on("input", (payload) => {
					updateProgress(xfer);
					FILE_BUFFER.push( new Uint8Array(payload) );
				});

				xfer.accept().then(
					() => {
						saveFile(xfer, FILE_BUFFER);
						term.write("\r\n");
						//socket.send(JSON.stringify({ type: "ignore", data: utoa("\r\n" + xfer.get_details().name + " was download success\r\n") }));
					},
					console.error.bind(console)
				);
			}

			on_form_submit();

		});

		let promise = new Promise( (res) => {
			zsession.on("session_end", () => {
				res();
			});
		});

		zsession.start();
		return promise;
	}

     let zsentry = new Zmodem.Sentry( {
        to_terminal: function(octets) {},  //i.e. send to the terminal

        on_detect: function(detection) {
            let zsession = detection.confirm();
            let promise;
            if (zsession.type === "receive") {
                promise = downloadFile(zsession);
            } else {
                promise = uploadFile(zsession);
            }
            promise.catch( console.error.bind(console) ).then( () => {
                //
            });
        },

        on_retract: function() {},

        sender: function(octets) { sock.send(new Uint8Array(octets)) },
     });

    // ?????? websocket ??????, ?????? web ??????
    sock.addEventListener('open', function () {
        $('#form').addClass('hide');
        $('#django-webssh-terminal').removeClass('hide');
        term.open(document.getElementById('terminal'));
		term.focus();
		$("body").attr("onbeforeunload",'checkwindow()'); //??????????????????????????????
		
    });

    // ?????????????????????????????????????????? web ??????
    sock.addEventListener('message', function (recv) {
        if (typeof(recv.data) === 'string') {
            let data = JSON.parse(recv.data);
            let message = data.message;
            let status = data.status;
            if (status === 0) {
                term.write(message)
            } else {
                //window.location.reload() ???????????????????????????
                //term.clear()
                term.write(message);
                $("body").removeAttr("onbeforeunload"); //??????????????????????????????

                // $(document).keyup(function(event){	// ????????????????????????
                // 	if(event.keyCode === 13){
                //         window.location.reload();
                // 	}
                // });
                // term.dispose();
                // $('#django-webssh-terminal').addClass('hide');
                // $('#form').removeClass('hide');
            }
        } else {
		    zsentry.consume(recv.data);
        }
    });

    /*
    * status ??? 0 ???, ?????????????????????????????? websocket ???????????????, data ??????????????????, ?????? cols ??? rows ??????
    * status ??? 1 ???, resize pty ssh ????????????, cols ??????????????????????????????, rows ??????????????????????????????, ?????? data ??????
    */
    let message = {'status': 0, 'data': null, 'cols': null, 'rows': null};
    let items = [];

    // ???????????????????????????
    term.onData(function (data) {
        // if (data !== '\r') {
        //     items.push(data)
        // }else {
        //     items.push(data);
        //     message['status'] = 0;
        //     message['data'] = items.join('');
        //     items = [];
        //     let send_data = JSON.stringify(message);
        //     sock.send(send_data);
        //     console.log(send_data)
        // }
        message['status'] = 0;
        message['data'] = data;
        let send_data = JSON.stringify(message);
        sock.send(send_data);
    });

    // ?????????????????????, ?????????????????????????????????????????????
    $(window).resize(function () {
        let cols = get_term_size().cols;
        let rows = get_term_size().rows;
        message['status'] = 1;
        message['cols'] = cols;
        message['rows'] = rows;
        let send_data = JSON.stringify(message);
        sock.send(send_data);
        term.resize(cols, rows)
    })
}

